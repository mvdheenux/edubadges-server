from django.conf.urls import url
from django.views.decorators.clickjacking import xframe_options_exempt
from rest_framework.urlpatterns import format_suffix_patterns

from .public_api import (IssuerJson, IssuerBadgesJson, IssuerImage, BadgeClassJson,
                         BadgeClassImage, BadgeClassCriteria, BadgeInstanceJson,
                         BadgeInstanceImage, BakedBadgeInstanceImage,
                         BadgeClassPublicKeyJson, IssuerPublicKeyJson, AssertionValidate)

json_patterns = [
    url(r'^issuers/(?P<entity_id>[^/.]+)$', xframe_options_exempt(IssuerJson.as_view(slugToEntityIdRedirect=True)), name='issuer_json'),
    url(r'^issuers/(?P<entity_id>[^/.]+)/pubkey/(?P<public_key_id>[^/.]+)$', xframe_options_exempt(IssuerPublicKeyJson.as_view(slugToEntityIdRedirect=True)), name='issuer_public_key_json'),
    url(r'^issuers/(?P<entity_id>[^/.]+)/badges$', xframe_options_exempt(IssuerBadgesJson.as_view(slugToEntityIdRedirect=True)), name='issuer_badges_json'),
    url(r'^badges/(?P<entity_id>[^/.]+)$', xframe_options_exempt(BadgeClassJson.as_view(slugToEntityIdRedirect=True)), name='badgeclass_json'),
    url(r'^badges/(?P<entity_id>[^/.]+)/pubkey/(?P<public_key_id>[^/.]+)$', xframe_options_exempt(BadgeClassPublicKeyJson.as_view(slugToEntityIdRedirect=True)), name='badgeclass_public_key_json'),
    url(r'^assertions/(?P<entity_id>[^/.]+)$', xframe_options_exempt(BadgeInstanceJson.as_view(slugToEntityIdRedirect=True)), name='badgeinstance_json'),
    url(r'^assertions/validate/(?P<entity_id>[^/]+)$', xframe_options_exempt(AssertionValidate.as_view()), name='assertion_validate'),
]

image_patterns = [
    url(r'^issuers/(?P<entity_id>[^/]+)/image$', IssuerImage.as_view(slugToEntityIdRedirect=True), name='issuer_image'),
    url(r'^badges/(?P<entity_id>[^/]+)/image', BadgeClassImage.as_view(slugToEntityIdRedirect=True), name='badgeclass_image'),
    url(r'^badges/(?P<entity_id>[^/]+)/criteria', BadgeClassCriteria.as_view(slugToEntityIdRedirect=True), name='badgeclass_criteria'),
    url(r'^assertions/(?P<entity_id>[^/]+)/image', BadgeInstanceImage.as_view(slugToEntityIdRedirect=True), name='badgeinstance_image'),
    url(r'^assertions/(?P<entity_id>[^/]+)/baked', BakedBadgeInstanceImage.as_view(slugToEntityIdRedirect=True), name='badgeinstance_bakedimage'),
]

urlpatterns = format_suffix_patterns(json_patterns, allowed=['json']) + image_patterns
