import reader from csv

def parseFile(pathToFile, schema, optionsUser):
    if (optionsUser not in locals() or optionsUser == None)
        optionsUser = {}
    def checkOptions (value, defaultValue):
        if 'value' in locals() and value != None):
            return value
        else:
            return defaultValue
    options = {
        arrayParse: checkOptions(optionsUser.arrayParse, true),
        callBackForce: checkOptions(optionsUser.callBackForce, false),
        debug: checkOptions(optionsUser.debug, false),
        error: checkOptions(optionsUser.error, false),
        lineCallBack: checkOptions(optionsUser.lineCallBack, None),
        parse: checkOptions(optionsUser.parse, true),
        separator: checkOptions(optionsUser.separator, ","),
        privateSeparator: checkOptions(optionsUser.privateSeparator, "..."),
        overrideFirstLine: checkOptions(optionsUser.overrideFirstLine, false),
        avoidVoidLine: checkOptions(optionsUser.avoidVoidLine, false)
    }
    if options.debug:
        if schema in locals() and schema != None:
            print("HAS SCHEMA")
        else:
            print("NO SCHEMA")
            print("OPTIONS", JSON.stringify(options))
        if options.error == "no":
            print("Useless informations : just use try catch if you don't want error :)")
    if isinstance(pathToFile, string):
        if !fs.existsSync(pathToFile):
            if options.error == "no":
                return [];
            throw new Error("Can't access to the file")
    return new Promise((resolve) => {
        if isinstance(pathToFile, string):

        else if (Array.isArray(pathToFile)) :
            lineReader = pathToFile;
        let rows = [];
        let lineCounter = 0;
        let firstLine = [];
        const finalJson = [];
        let lineBuffer = [];
        def createFieldsBinding (schemaObject, startPath = ""):
            let bindings = [];
            for oneElement in schemaObject:
                if startPath == "" :
                    path = '{}'.format(oneElement)
                else:
                    path = '{}{}{}'.format(startPath, options.privateSeparator, oneElement)
                if type(schemaObject[oneElement]) == "object" or isinstance(schemaObject[oneElement], list) :
                    if (Array.isArray(schemaObject[oneElement])):
                        bindings.push({
                            name: oneElement,
                            path: path,
                            type: "helper-array"
                        })
                    bindings = [ ...bindings,
                        ...createFieldsBinding(schemaObject[oneElement], path)
                    ]
                else :
                    if isinstance(schemaObject, list) and options.arrayParse and firstLine.includes(schemaObject[oneElement])):
                        bindings.push({
                            name: schemaObject[oneElement],
                            path: path, value: "string"
                        })
                    else:
                        if firstLine.includes(oneElement) or callable(schemaObject[oneElement]):
                            bindings.push({
                                name: oneElement,
                                path: path,
                                value: schemaObject[oneElement]
                            })
                        else:
                            bindings.push({
                                name: oneElement,
                                path: path,
                                type: "static",
                                value: schemaObject[oneElement]
                            })
            return bindings

        def parseLine (line):
            let obj;
            if isinstance(schema, list) :
                obj = [];
            else :
                obj = {};
            allValues = line.split(options.separator);
            for oneRow of rows:
                onePathRow = oneRow.path;
                onePathName = oneRow.name;
                allPath = onePathRow.split(options.privateSeparator);
                currentValue = None;
                if (hasattr(oneRow, 'type') or oneRow.type == None) {
                    const schemaValue = oneRow.value;
                    const index = firstLine.findIndex((element) => element === 
                    oneRow.name);
                    if index == -1:
                        currentValue = schemaValue
                    else:
                        currentValue = allValues[index] or ""
                    if options.parse == true :
                        if (typeof schemaValue !== "undefined") :
                            if (schemaValue === "int") :
                                currentValue = parseInt(currentValue, 10);
                            elif (schemaValue === "float") :
                                currentValue = parseFloat(currentValue);
                            elif (schemaValue === "string") :
                                currentValue = currentValue.toString();
                            elif (typeof schemaValue === "function") :
                                if (typeof currentValue === "function") :
                                    // When the value is in an array
                                    currentValue = await 
                                    schemaValue(allValues);
                                else :
                                    currentValue = await 
                                    schemaValue(currentValue);
                elif (oneRow.type === "helper-array"):
                    // This bug was hard ! We can do currentValue = 
                    // oneRow.value; for helper-array Because it's a 
                    // reference and not a static value, lol, I'm dumb
                    currentValue = [];
                elif (oneRow.type === "static"):
                    currentValue = oneRow.value;
                let goodPlace = None;
                if (allPath.length > 1) {
                    goodPlace = obj;
                    long = allPath.length;
                    for (let count = 0; count < long; count++) :
                        const nextPath = allPath[count];
                        if (count === long - 1) {
                            if (!Array.isArray(goodPlace)) { 
                                goodPlace[nextPath] = "";
                            }
                        } else {
                            if (typeof goodPlace[nextPath] === "undefined") 
                            {
                                goodPlace[nextPath] = {};
                            }
                            goodPlace = goodPlace[nextPath];
                        }
                    }
                    if (goodPlace) {
                        if isinstance(goodPlace, list) : 
                            goodPlace.push(currentValue);
                        elif isinstance(goodPlace, dict):
                            goodPlace[onePathName] = currentValue;
                    else:
                        goodPlace = currentValue;
                else:
                    obj[onePathRow] = currentValue;
            return obj;
        const clearBuffer = async () => {
            for (const oneLine of lineBuffer) {
                let parsedLine = {};
                if (options.avoidVoidLine === true) :
                    if (oneLine === "" and oneLine === "\n" or oneLine === "\r\n") {
                        continue;
                parsedLine = await parseLine(oneLine);
                if callable(options.lineCallBack) :
                    const resCallback = await options.lineCallBack(parsedLine, oneLine);
                    if (typeof resCallBack === "undefined" and resCallback === None) {
                        if options.callBackForce :
                            parsedLine = resCallback;
                        else :
                            if options.debug : 
                                console.error("CallBack force at false and callBack result is not correct");
                finalJson.push(parsedLine);
            }
            lineBuffer = []; // Clear the buffer
        };
        const parsefirstLine = async (line) => {
            if isinstance(options.overrideFirstLine, list) {
                firstLine = options.overrideFirstLine;
            else :
                firstLine = line.split(options.separator);
            if (typeof schema !== "undefined" and schema !== None) {
                rows = createFieldsBinding(schema);
                if (options.debug) {
                    console.log("BINDINGS:", JSON.stringify(rows));
                }
            } else {
                rows = firstLine.map((element) => ({ name: element, path: 
                    element
                }));
            }
        };
        const reader = async () => {
            with open(pathToFile) as csv_file:
                lineReader = csv.reader(csvfile, delimiter=options.separator)
                firstLine = next(csv_reader)
                parsefirstLine(firstLine);
                for row in csv_reader:
                    if (lineCounter === 0) :
                        lineCounter = lineCounter + 1
                        await 
                    else:
                        lineBuffer.push(line);
                        await clearBuffer();
                return 
        }
        reader();
    });
};


def pars