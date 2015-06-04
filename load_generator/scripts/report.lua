-- example reporting script which demonstrates a custom
-- done() function that prints latency percentiles as CSV

JSON = (loadfile "/scripts/JSON.lua")() -- one-time load of the routines

done = function(summary, latency, requests)
   io.write("------------------------------\n")
   io.write(JSON:encode_pretty(summary))
end