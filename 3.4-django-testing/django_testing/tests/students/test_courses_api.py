import pytest
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_204_NO_CONTENT
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
    url = reverse('courses-list') + f'{filter_id}/'
    resp = client.get(url)
    assert resp.status_code == HTTP_200_OK
    results = resp.json()
    assert results
    assert courses[0].id == results['id']


@pytest.mark.django_db
def test_name_filter_courses(client, course_factory):
    quantity = 2
    name = 'Example Name'
    courses = course_factory(_quantity=quantity, name=name)
    course_factory(_quantity=5)
    url = reverse('courses-list') + f'?name={name}'
    resp = client.get(url)
    assert resp.status_code == HTTP_200_OK
    results = resp.json()
    assert results
    assert len(results) == quantity
    assert courses[0].name == results[0]['name']


@pytest.mark.django_db
def test_create_course(client, student_factory):
    name = 'Example Name'
    students = [item.id for item in student_factory(_quantity=2)]
    course_json = {
        'name': name,
        'students': students
    }
    url = reverse('courses-list')
    resp = client.post(url, data=course_json)
    assert resp.status_code == HTTP_201_CREATED
    results = resp.json()
    assert results['name'] == name
    assert len(results['students']) == len(students)


@pytest.mark.django_db
def test_update_course(client, course_factory, student_factory):
    name = 'Example Name'
    students = [item.id for item in student_factory(_quantity=2)]
    course = course_factory()
    update_json = {
        'name': name,
        'students': students
    }
    url = reverse('courses-list') + f'{course.id}/'
    resp = client.patch(url, data=update_json)
    assert resp.status_code == HTTP_200_OK
    results = resp.json()
    assert results['name'] == name
    assert len(results['students']) == len(students)


@pytest.mark.django_db
def test_delete_course(client, course_factory, student_factory):
    course = course_factory()
    url = reverse('courses-list') + f'{course.id}/'
    resp = client.delete(url)
    assert resp.status_code == HTTP_204_NO_CONTENT
