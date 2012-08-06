pastebin-find
=============

Python script to monitor new Pastebin pastes for a provided search term

Usage: python pastefind.py search_regex

Edit the "time_between" variable to change the time between requests. Currently it is at 5s. If the value is too low, pastebin may block your IP address for repeated queries. If it is too high, you may miss a paste since the program only scans the top 10 pastes on the recently added page.

Regex should be the regex itself in quotes. For example, to search for formatted phone numbers, use '\(?(\d{3})\)?-?(\d{3})-(\d{4})' as the search input.
