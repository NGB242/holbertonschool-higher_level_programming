#!/usr/bin/env python3
import requests


def get_posts():
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    print(response.json())
    
if response.status_code == 200:
    posts = response.json()

for post in posts:
    print(post['title'])

def fetch_and_save_posts():
response = requests.get("https://jsonplaceholder.typicode.com/posts")

if response.status_code == 200:
    posts = response.json()

structured_data = [{'id': post['id'], 'title': post['title'], 'body': post['body']} for post in posts]

with open('posts.csv', 'w', newline='') as csvfile:
    fieldnames = ['id', 'title', 'body']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(structured_data)

fetch_and_print_posts()
fetch_and_save_posts()
