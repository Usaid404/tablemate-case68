# TableMate - restaurant table reservation prototype (waitlist ordering)
# FR-05 overbooking uses max_bookings(capacity, 0.18)

## Running the tests

Python 3 is required.

Run the unit and integration test suite from the project root:

```bash
python -m unittest discover -s tests -v
```

The test suite covers helper functions, waitlist ordering, tie-breaking, booking capacity, no-show handling and service integration.
