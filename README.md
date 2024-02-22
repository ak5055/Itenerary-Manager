# Itenary-Manager

<ul>
  <li>
Itenary Planner (interacts with firstore NoSQL serverless database of GCP):
    <ul>
<li>GET /getItenaries/***REMOVED***userId***REMOVED***:
  <ul>
<li>Query params:<ul>
<li>Itinerary id: string For getting only a single itinerary of user</li>
<li>Per_page: int For page size </li>
<li>Page: int For page number</li></ul></li></ul></li>
<li>POST /createItenary: Creates itinerary of user <ul>
<li>Body:<ul>
<li>Userid: string</li>
<li>Flights: list of flight objects</li>
<li>Hotels: list of hotel objects</li>
<li>Tourism: list of tourist activities</li></ul></li></ul></li>
<li>PUT /updateItenary: Updates itinerary of user
  <ul>
    <li>Body:<ul>
<li>Userid: string</li>
<li>Itenaryid: string</li>
    </ul></li></ul></li>
    <li>DELETE /deleteItenary:<ul>
<li>Body:<ul>
<li>Userid: string</li>
<li>Itenaryid: string</li>
</ul></li> </ul> </li> </ul></li>
</ul>
