# PRODUCTION SCHEDULER BACKEND SERVER #

# About #
A Flask Server for a fullstack project sourced from the coding canal's coding challenge on github. This is a production scheduler with 3 independent machine resources (CNC machine, Assembly Line A, Assembly Line B) capable of taking orders and producing and recording the inventory.

- Technologies, Libraries and frameworks used includes; Next.js, Typescript, Tailwind CSS, Flask Python, PostgreSQL, Recharts.js, Zod validator, and Tanstack table.

# API routes#
* "/orders" : takes in http requests for "GET, POST, and DELETE" to process them by querying a postgresql database for the requested data or insert new data and returns results in JSON format to the frontend. It also processes and deletes specified orders from the database when requested.
* "/check_collision" : this API route accepts http requests from the Zod validator in the  frontend seeking to check if the parameters from a newly booked order is colluding with an existing one in the database via its start time, end time, and date and returns a message  if the conditions meet.
