import requests
import itertools

url = "https://hydra-streams-staging.vnerd.com"
part_status_alias = "partition_statuses"
group_offset = "groupOffset"
high_offset = "largestOffset"

import random
import json


def restart_jobs_continually(ids):
    for id in itertools.cycle(ids):
        r = requests.post(url+"/jobs/{}/stop".format(id))
        r.raise_for_status()
        print(r.text)
        r2 = requests.post(url+"/jobs/{}/start".format(id))
        r2.raise_for_status()
        print(r2.text)


def restart_job(guid):
    r = requests.post(url + "/jobs/{}/stop".format(guid))
    r.raise_for_status()
    print(r.text)
    r2 = requests.post(url + "/jobs/{}/start".format(guid))
    r2.raise_for_status()
    print(r2.text)


import ast

def get_jobs(limit=1000, randomize=False):
    res = requests.get(url+"/jobs")
    res.raise_for_status()
    jobs_array = ast.literal_eval(res.text)
    if limit >= len(jobs_array):
        limit = len(jobs_arr)

    if randomize:
        random.shuffle(jobs_array)

    return jobs_array[:limit]

def add_status_to_job(job):
    job[part_status_alias] = []
    res = requests.get(url + "/jobs/{}/status".format(job["jobId"]))
    res.raise_for_status()
    res_obj = ast.literal_eval(res.text)
    for key in res_obj.keys():
        partitions = res_obj[key]
        for part in partitions:
            job[part_status_alias].append(part)
    #print(job)
    return job

jobs_arr = get_jobs(limit=40, randomize=True)
job_and_statuses = []
for job in jobs_arr:
    job_and_status = add_status_to_job(job)
    job_and_statuses.append(job_and_status)


def is_bad_replication_job(job_and_status):
    for js in job_and_statuses:
        for part in js[part_status_alias]:
            print(part)
            diff = float(part[group_offset])/float(part[high_offset])
            print(diff)
            if diff < .99997:
                print("job {} is behind!!".format(js["jobId"]))
                restart_job(js["jobId"])


def is_bad_replication_job_running(job_and_status):
    for js in job_and_statuses:
        for part in js[part_status_alias]:
            #print(part)
            diff = float(part[group_offset])/float(part[high_offset])
            #print(diff)
            if diff < .99997 and js["status"] == "Running":
                #print("job {} is behind!!".format(js["jobId"]))
                return True
    return False

def is_errored_job(job):
    if job["status"] in {"error", "Error"}:
        return True
    return False


def print_bad_jobs(jobs):
    print(jobs["jobId"])


def restart_behind_jobs(job_and_statuses):
    for js in job_and_statuses:
        if is_bad_replication_job_running(js):
            print_bad_jobs(js)
            restart_job(js["jobId"])


def print_error_jobs(job_and_statuses):
    for js in job_and_statuses:
        if is_errored_job(js):
            print(js["jobId"])


print_error_jobs(job_and_statuses)
