# CellMapper_CSV_Visualizer
 Visualizing the CSV output file from the app "CellMapper"
 
 
## CSV data structure
 from [CellMapper Documentation](https://www.cellmapper.net/CellMapper_CSV)
 
 
| Name       | Required | Description                                                |
| ---------- | -------- | ---------------------------------------------------------- |
| latitude   | \*       | Latitude of data point in Decimal Degrees (ex. 49.231)     |
| longitude  | \*       | Longitude of data point in Decimal Degrees (ex. -123.1232) |
| altitude   | \*       | Altitude, in metres                                        |
| MCC        | \*       | Mobile Country Code                                        |
| MNC        | \*       | Mobile Network Code                                        |
| LAC        | \*       | Location Area Code / Tracking Area Code (TAC)              |
| CID        | \*       | Full Cell ID / Cell Identifier (CI, not CGI for LTE)       |
| Signal     | \*       | RSSI Signal strength in dBm / RSRP for LTE                 |
| type       | \*       | one of: GSM,UMTS,CDMA, or LTE                              |
| subtype    | \*       | 1)                                                         |
| ARFCN      |          | Number representing 3GPP ARFCN/EARFCN/UARFCN (frequency)   |
| PSC or PCI |          | UMTS Primary Scrambling Code or LTE Physical Cell Identity |


1) 
for GSM above: GPRS, EDGE 
for UMTS above: UMTS, HSDPA, HSUPA, HSPA, HSPA+, DC-HSPA+ 
for LTE above: LTE, LTE-A 
for CDMA above: CDMA, 1xRTT, EVDO, EHRPD