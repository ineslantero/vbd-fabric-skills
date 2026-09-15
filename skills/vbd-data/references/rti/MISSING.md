# Missing RTI data CSVs

No RTI-specific CSV files were retrievable from the SharePoint cache. The Real-Time Intelligence lab in the SharePoint IP release generates its data through an Eventstream sample generator (Bicycles rentals / stock trades / weather feed) rather than shipping CSV seed files.

## What to do

The tutorial (`skills/vbd-lab-foundation/references/rti/rti-tutorial.md`) uses the Fabric **built-in sample streams** (Bicycles, Stocks, YellowTaxi, or a custom event producer). No CSV reference is needed for the lab itself.

If you want CSV shape references for `/vbd-data` to model the customer's streaming data on:

- **Bicycles sample** — schema is exposed in the Eventstream editor (BikepointID, Street, Neighbourhood, Latitude, Longitude, No_Bikes, No_Empty_Docks, Timestamp).
- **Stock market sample** — Symbol, Price, DateTime, Volume, Change.

Recreate a small CSV per your customer domain (e.g. IoT sensor readings, transaction stream, click stream) directly during `/vbd-data`.
