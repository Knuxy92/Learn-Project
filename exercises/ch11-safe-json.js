const safeJsonParse = (jsonText) => {
  try {
    return JSON.parse(jsonText);
  } catch (e) {
    return { error: 'Invalid JSON' };
  }
};

const getUserNameFromJson = (jsonText) => {
  const JsonParse = safeJsonParse(jsonText);
  if (JsonParse === undefined || JsonParse.name === undefined) return "Unknown user";
  return JsonParse.name
};

const parseWithFinally = (jsonText) => {
  try {
    return JSON.parse(jsonText);
  } catch (e) {
    return null
  } finally {
    console.log('Finished parsing')
  }
};

const validJson = '{"name":"Knuxy92","age":17}';
const invalidJson = '{name:"Knuxy92"}';

console.log("Safe parse valid:", safeJsonParse(validJson));
console.log("Safe parse invalid:", safeJsonParse(invalidJson));
console.log("User name valid:", getUserNameFromJson(validJson));
console.log("User name invalid:", getUserNameFromJson(invalidJson));
console.log("Parse with finally valid:", parseWithFinally(validJson));
console.log("Parse with finally invalid:", parseWithFinally(invalidJson));
