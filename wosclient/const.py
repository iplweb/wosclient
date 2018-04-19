# Template for fetching ids and timesCited from AMR
id_request_template = """<?xml version="1.0" encoding="UTF-8" ?>
<request xmlns="http://www.isinet.com/xrpc41" src="app.id={appId}">
  <fn name="LinksAMR.retrieve">
    <list>
      <!-- authentication -->
      <map>
        <val name="username">{user}</val>
        <val name="password">{password}</val>
      </map>
      <!-- what to to return -->
       <map>
         <list name="WOS">
           <val>sourceURL</val>
           <val>ut</val>
           <val>doi</val>
           <val>pmid</val>
           <val>timesCited</val>
         </list>
       </map>
       <!-- LOOKUP DATA -->
       {items}
    </list>
  </fn>
</request>
"""

AMR_URL = "https://ws.isiknowledge.com/cps/xrpc"

BATCH_SIZE = 50

ALLOWED_KEYS = ['pmid', 'doi']
