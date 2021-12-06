from csv import reader as CSVreader
from os.path import isfile
from json import dumps as JSONstringify


def parseFile(pathToFile="", schema=None, optionsUser={}):
    def checkOptions(optionsUser, attr, defaultValue):
        if hasattr(optionsUser, attr) or (attr == "lineCallBack" and callable(optionsUser[attr])):
            return optionsUser[attr]
        else:
            return defaultValue
    options = {
        "arrayParse": checkOptions(optionsUser, "arrayParse", True),
        "callBackForce": checkOptions(optionsUser, "callBackForce", False),
        "debug": checkOptions(optionsUser, "debug", False),
        "error": checkOptions(optionsUser, "error", False),
        "lineCallBack": checkOptions(optionsUser, "lineCallBack", None),
        "parse": checkOptions(optionsUser, "parse", True),
        "separator": checkOptions(optionsUser, "separator", ","),
        "privateSeparator": checkOptions(optionsUser, "privateSeparator", "..."),
        "overrideFirstLine": checkOptions(optionsUser, "overrideFirstLine", False),
        "avoidVoidLine": checkOptions(optionsUser, "avoidVoidLine", False)
    }
    if options["debug"]:
        if schema in locals() and schema != None:
            print("HAS SCHEMA")
        else:
            print("NO SCHEMA")
            print("OPTIONS", JSONstringify(options))
        if options["error"] == "no":
            print("Useless informations : just use try catch if you don't want error :)")
    if isinstance(pathToFile, str):
        if isfile(pathToFile):
            if options["error"] == "no":
                return []
            # throw new Error("Can't access to the file")

        if isinstance(pathToFile, str):
            csvFile = open(pathToFile)
            lineReader = CSVreader(csvFile, delimiter=options["separator"])
        elif isinstance(pathToFile, list):
            lineReader = pathToFile
        rows = []
        firstLine = []

        def createFieldsBinding(schemaObject, startPath=""):
            global firstLine
            bindings = []
            for oneElement in schemaObject:
                if startPath == "":
                    path = '{}'.format(oneElement)
                else:
                    path = '{}{}{}'.format(
                        startPath, options["privateSeparator"], oneElement)
                if isinstance(schemaObject[oneElement], dict) or isinstance(schemaObject[oneElement], list):
                    if isinstance(schemaObject[oneElement], list):
                        bindings.append({
                            "name": oneElement,
                            "path": path,
                            "type": "helper-array"
                        })
                    bindings = [
                        *bindings, *createFieldsBinding(schemaObject[oneElement], path)]
                else:
                    if isinstance(schemaObject, list) and options.arrayParse and schemaObject[oneElement] in firstLine:
                        bindings.append({
                            "name": schemaObject[oneElement],
                            "path": path,
                            "value": "string"
                        })
                    else:
                        if oneElement in firstLine or callable(schemaObject[oneElement]):
                            bindings.append({
                                "name": oneElement,
                                "path": path,
                                "value": schemaObject[oneElement]
                            })
                        else:
                            bindings.append({
                                "name": oneElement,
                                "path": path,
                                "type": "static",
                                "value": schemaObject[oneElement]
                            })
            return bindings

        def parseLine(line):
            global rows
            global firstLine
            if isinstance(schema, list):
                obj = []
            else:
                obj = {}
            allValues = line
            for oneRow in rows:
                onePathRow = oneRow["path"]
                onePathName = oneRow["name"]
                allPath = onePathRow.split(options["privateSeparator"])
                currentValue = None
                if (not hasattr(oneRow, 'type')) or (hasattr(oneRow, 'type') and oneRow["type"] == None):
                    schemaValue = oneRow["value"]
                    index = firstLine.index(oneRow["name"])
                    if index == -1:
                        currentValue = schemaValue
                    else:
                        currentValue = allValues[index] or ""
                    if options["parse"] == True:
                        if schemaValue == "int":
                            currentValue = int(currentValue)
                        elif schemaValue == "float":
                            currentValue = float(currentValue)
                        elif schemaValue == "string":
                            currentValue = str(currentValue)
                        elif callable(schemaValue):
                            if callable(currentValue):
                                # When the value is in an array
                                currentValue = schemaValue(allValues)
                            else:
                                currentValue = schemaValue(currentValue)
                elif (hasattr(oneRow, 'type') and oneRow["type"] == "helper-array"):
                    currentValue = []
                elif (hasattr(oneRow, 'type') and oneRow["type"] == "static"):
                    currentValue = oneRow["value"]
                goodPlace = None
                if len(allPath) > 1:
                    goodPlace = obj
                    long = len(allPath)
                    for count in range(0, long):
                        nextPath = allPath[count]
                        if count == (long - 1):
                            if not isinstance(goodPlace, list):
                                goodPlace[nextPath] = ""
                        else:
                            if not hasattr(goodPlace, nextPath):
                                goodPlace[nextPath] = {}
                            goodPlace = goodPlace[nextPath]
                    if goodPlace:
                        if isinstance(goodPlace, list):
                            goodPlace.append(currentValue)
                        elif isinstance(goodPlace, dict):
                            goodPlace[onePathName] = currentValue
                    else:
                        goodPlace = currentValue
                else:
                    obj[onePathRow] = currentValue
            return obj

        def parsefirstLine():
            global firstLine
            if isinstance(options["overrideFirstLine"], list):
                firstLine = options["overrideFirstLine"]
            if isinstance(schema, dict):
                cols = createFieldsBinding(schema)
                if options["debug"]:
                    print("BINDINGS:", JSONstringify(cols))
            else:
                def dupli(element):
                    return {
                        "name": element,
                        "type": element
                    }
                cols = map(dupli, firstLine)
            return cols

        def reader():
            global rows
            global firstLine
            finalJson = []
            firstLine = next(lineReader)
            rows = parsefirstLine()
            for oneLine in lineReader:
                parsedLine = {}
                if options["avoidVoidLine"] == True:
                    if oneLine == "" and oneLine == "\n" or oneLine == "\r\n":
                        continue
                parsedLine = parseLine(oneLine)
                if callable(options["lineCallBack"]):
                    resCallback = options["lineCallBack"](parsedLine, oneLine)
                    if resCallback == None:
                        if options["callBackForce"]:
                            parsedLine = resCallback
                        else:
                            if options["debug"]:
                                print(
                                    "CallBack force at False and callBack result is not correct")
                    else:
                        parsedLine = resCallback
                finalJson.append(parsedLine)
            return finalJson
        converted = reader()
        if isinstance(pathToFile, str):
            csvFile.close()
        return converted
