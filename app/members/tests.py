from django.contrib.auth import get_user_model
from django.db import IntegrityError
from django.test import TestCase, TransactionTestCase

from members.exceptions import RelationNotExist, DuplicateRelationException

User = get_user_model()


# Create your tests here.
# 테스트 코드를 작성하기위해서는
# 장고에서 모듈 이름을 tests.py로 요구하고
# TestCase를 상속, def test_ 를 요구한다
class RelationTestCase(TransactionTestCase):
    def create_dummy_user(self, num):
        return [User.objects.create_user(username=f'u{x+1}') for x in range(num)]

    def test_follow(self):
        """
        특정 유져가 다른 유져를 팔로우 했을 경우, 정상 작동하는지 확인
        :return:
        """

        # 유져 2명 생성

        # u1이 u2를 팔로우
        # relation = u1.relations_by_from_user.create(to_user=u2, relation_type='f')
        #
        # relation = u1.relations_by_from_user.create(to_user=u2, relation_type='f')
        u1, u2 = self.create_dummy_user(2)
        u1.follow(u2)
        # u1의 팔로윙에 u2가 포함되어있는지 확인
        self.assertIn(u2, u1.following)

        self.assertTrue(u1.following_relations.filter(to_user=u2).exists())

    def test_follow_only_once(self):
        u1, u2 = self.create_dummy_user(2)
        u1.follow(u2)
        # u1.follow(u2)

        # self.assertRaises(IntegrityError, u1.follow(), u2)
        with self.assertRaises(DuplicateRelationException):
            u1.follow(u2)

        self.assertEqual(u1.following.count(), 1)

    def test_unfollow_if_follow_exist(self):
        u1, u2 = self.create_dummy_user(2)

        u1.follow(u2)
        u1.unfollow(u2)

        self.assertNotIn(u2, u1.following)

    def test_unfollow_fail_if_follow_not_exist(self):
        u1, u2 = self.create_dummy_user(2)

        with self.assertRaises(RelationNotExist):
            u1.unfollow(u2)
