import pytest
from rest_framework.status import HTTP_200_OK
from django.urls import reverse


@pytest.mark.django_db
def test_get_first_course(client, course_factory):
    quantity = 1
    url = reverse('courses-list')
    courses = course_factory(_quantity=quantity)
    resp = client.get(url)
    assert resp.status_code == HTTP_200_OK
    results = resp.json()
    assert results
    assert len(results) == quantity
    assert courses[0].id == results[0]['id']
    assert courses[0].name == results[0]['name']


@pytest.mark.django_db
def test_get_some_courses(client, course_factory):
    quantity = 12
    url = reverse('courses-list')
    course_factory(_quantity=quantity)
    resp = client.get(url)
    assert resp.status_code == HTTP_200_OK
    results = resp.json()
    assert results
    assert len(results) == quantity


@pytest.mark.django_db
def test_id_filter_courses(client, course_factory):
    quantity = 12
    courses = course_factory(_quantity=quantity)
    filter_id = courses[0].id
    url = reverse('courses-list') + f'?id={filter_id}'
    resp = client.get(url)
    assert resp.status_code == HTTP_200_OK
    results = resp.json()
    assert results
    assert len(results) == 1
    assert courses[0].id == results[0]['id']


@pytest.mark.django_db
def test_name_filter_courses(client, course_factory):
    quantity = 2
    name = "Example Name"
    courses = course_factory(_quantity=quantity, name=name)
    course_factory(_quantity=5)
    url = reverse('courses-list') + f'?name={name}'
    resp = client.get(url)
    assert resp.status_code == HTTP_200_OK
    results = resp.json()
    assert results
    assert len(results) == quantity
    assert courses[0].name == results[0]['name']
