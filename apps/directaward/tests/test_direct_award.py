import json
from mainsite.tests import BadgrTestCase


class DirectAwardTest(BadgrTestCase):

    def test_create_single_direct_award(self):
        teacher1 = self.setup_teacher(authenticate=True,)
        self.setup_staff_membership(teacher1, teacher1.institution, may_create=True)
        faculty = self.setup_faculty(institution=teacher1.institution)
        issuer = self.setup_issuer(created_by=teacher1, faculty=faculty)
        badgeclass = self.setup_badgeclass(issuer=issuer)
        post_data = [{'recipient_email': 'some@email.com',
                     'eppn': 'some_eppn',
                     'badgeclass': badgeclass.entity_id}]
        response = self.client.post('/directaward/create', json.dumps(post_data),
                                    content_type='application/json')
        self.assertEqual(response.status_code, 201)

    def test_accept_direct_award(self):
        teacher1 = self.setup_teacher(authenticate=False)
        self.setup_staff_membership(teacher1, teacher1.institution, may_create=True)
        faculty = self.setup_faculty(institution=teacher1.institution)
        issuer = self.setup_issuer(created_by=teacher1, faculty=faculty)
        badgeclass = self.setup_badgeclass(issuer=issuer)
        student = self.setup_student(authenticate=True,
                                     affiliated_institutions=[teacher1.institution])
        direct_award = self.setup_direct_award(created_by=teacher1, badgeclass=badgeclass, recipient=student)
        post_data = {'accept': True}
        response = self.client.post('/directaward/accept/{}'.format(direct_award.entity_id),
                                    json.dumps(post_data),
                                    content_type='application/json')
        self.assertEqual(response.status_code, 201)

    def test_update_and_delete_direct_award(self):
        teacher1 = self.setup_teacher(authenticate=True)
        self.setup_staff_membership(teacher1, teacher1.institution, may_award=True)
        faculty = self.setup_faculty(institution=teacher1.institution)
        issuer = self.setup_issuer(created_by=teacher1, faculty=faculty)
        badgeclass = self.setup_badgeclass(issuer=issuer)
        student = self.setup_student(affiliated_institutions=[teacher1.institution])
        direct_award = self.setup_direct_award(created_by=teacher1, badgeclass=badgeclass, recipient=student)
        post_data = {'recipient_email': 'other@email.com'}
        response = self.client.put('/directaward/edit/{}'.format(direct_award.entity_id), json.dumps(post_data),
                                    content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(direct_award.__class__.objects.get(pk=direct_award.pk).recipient_email,
                         'other@email.com')
        response = self.client.delete('/directaward/edit/{}'.format(direct_award.entity_id),
                                      content_type='application/json')
        self.assertEqual(response.status_code, 204)
