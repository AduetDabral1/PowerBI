Base_API for Country data


  let
    // Define the API endpoint
    apiUrl = "https://serpapi.com/search.json",


// Define the parameters
queryParams = [ 
	engine = "google_trends", 
	q = Query_Keywords , 
	data_type = "GEO_MAP", 
	date = "today 5-y", 
	tz="-330",
	api_key = API_Key
],

// Combine the endpoint and parameters
fullUrl = apiUrl & "?" & Uri.BuildQueryString(queryParams),

// Make the HTTP request
response = Web.Contents(fullUrl),

// Parse the JSON response
jsonResponse = Json.Document(response),

// Convert the response to a table
dataTable = Table.FromRecords({jsonResponse}),

// Extract the relevant data
comparedBreakdownByRegion = dataTable{0}[compared_breakdown_by_region]
in
    comparedBreakdownByRegion




Base_API for data based on date


let
    // Define the base URL for the API call
    BaseUrl = "https://serpapi.com/search",

// Define the query parameters with engine, terms, data type, date, and time zone
QueryParams = [
	engine = "google_trends", 
	q = Query_Keywords,
	data_type = "TIMESERIES", 
	date = "all", 
	tz = "-330",    
	api_key = API_Key
],

// Generate the full URL with query parameters
UrlWithParams = BaseUrl & "?" & Text.Combine(List.Transform(Record.FieldNames(QueryParams), 
    each _ & "=" & Uri.EscapeDataString(Record.Field(QueryParams, _))), "&"),

// Fetch data from the API
JsonResponse = Json.Document(Web.Contents(UrlWithParams)),

// Extract the "interest_over_time" part from the JSON response
InterestOverTime = JsonResponse[#"interest_over_time"]
in
    InterestOverTime



Base_API for data based on date (last 7 days)


let
    // Define the base URL for the API call
    BaseUrl = "https://serpapi.com/search",

// Define the query parameters with engine, terms, data type, date, and time zone
QueryParams = [
	engine="google_trends",
	q=Query_Keywords, 
	data_type = "TIMESERIES",
	date = "now 7-d",
	tz = "-330",
	api_key = API_Key
],

// Generate the full URL with query parameters
UrlWithParams = BaseUrl & "?" & Text.Combine(List.Transform(Record.FieldNames(QueryParams), 
    each _ & "=" & Uri.EscapeDataString(Record.Field(QueryParams, _))), "&"),

// Fetch data from the API
JsonResponse = Json.Document(Web.Contents(UrlWithParams)),

// Extract the "interest_over_time" part from the JSON response
InterestOverTime = JsonResponse[#"interest_over_time"]
in
    InterestOverTime



Base_API for related keywords

let
    // Define the API endpoint
    apiUrl = "https://serpapi.com/search.json",

// Define the parameters
queryParams = [
	engine = "google_trends",
	q = "The Developer",
	data_type = "RELATED_TOPICS",
	api_key = API_Key
],

// Combine the endpoint and parameters to create the full URL
fullUrl = apiUrl & "?" & Uri.BuildQueryString(queryParams),

// Make the HTTP request and get the response
response = Web.Contents(fullUrl),

// Parse the JSON response
jsonResponse = Json.Document(response)
in
    jsonResponse