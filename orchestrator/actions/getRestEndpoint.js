/*
  General
    Name: getRestEndpoint
    Module: com.vmware.library.vco

  Script
    Runtime Environment: JavaScript
    Inputs: 
      restHostname : string

  Source(s): 
    https://adrian.heissler.at/2023/03/consuming-the-nsx-t-api-with-aria-automation-and-orchestrator/
*/
var restHost = null;
for each (restHostFinder in RESTHostManager.getHosts()){
    var host = RESTHostManager.getHost(restHostFinder);
    if(host.name === restHostname){
        restHost = host;
        break;
    }
}

if (restHost == null){
    throw "REST host not found";
}

return restHost;
