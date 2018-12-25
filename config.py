''' Configure threading in port scanner '''

# Number of allowed threads (default: 100)
number_threads = 100

# Number of jobs assigned (default: 1000, total: 65535)
# Caution: scan will take longer with more jobs assigned:
# - 2500 jobs: approx. 11 seconds
# - 5000 jobs: approx. 24 seconds

number_jobs = 1000
