#!/usr/bin/env python3
""" End-to-end integration test.
    Use assert to validate the response’s expected
    status code and payload (if any) for each task
"""
import requests
URL = 'http://localhost:5000'


def register_user(email: str, password: str) -> None:
    """ test """
    data = {"email": email, "password": password}
    response = requests.post(f'{URL}/users', data=data)
    assert response.status_code == 200, "Test fail"
    print("Task validate: 'register_user'")
