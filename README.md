The goal of this project is to daily scrape proxynova for new anonimity proxy servers.

The project description:
	1. for parse the proxy ip from proxynova.com page it was created a decoder function (there all ip are encoded with Dean Edwars packer)
	2. there was created an exporter into csv format (added into extensions)
	3. in the item pipeline every item is verified for an existent copy downloaded in the past. If exist that item is dopped
	4. the result of the project is a csv file with a list os proxy ip and port
