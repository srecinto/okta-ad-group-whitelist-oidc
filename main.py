import config
import json

from utils.rest import OktaUtil

"""
GLOBAL VARIABLES ########################################################################################################
"""

"""
UTILS ###################################################################################################################
"""


def get_ad_groups_from_okta():
    print "get_ad_groups_from_okta"
    filtered_groups = []
    okta_util = OktaUtil(config.okta)
    # Get all external groups i.e. google, salesforce, AD, LDAP
    groups = okta_util.search_groups("type eq \"APP_GROUP\"")

    # filter out all other external groups except windows Security groups
    for group in groups:
        for object_class in group["objectClass"]:
            if object_class == "okta:windows_security_principal":
                filtered_groups.append(group)

    return filtered_groups


def whitelist_app(white_list_group_ids):
    print "whitelist_app()"
    okta_util = OktaUtil(config.okta)

    app_id = config.okta["oidc_appid"]

    # Get the application to add the whitelist to
    application = okta_util.get_application(app_id)

    # Update the application with the whitelist
    application["profile"] = {
        "groupwhitelist": white_list_group_ids
    }

    response = okta_util.update_application(app_id, application)

    print "Okta App Update Response: {0}".format(json.dumps(response, indent=4, sort_keys=True))

    return "COMPLETED"


"""
MAIN ##################################################################################################################
"""
if __name__ == "__main__":
    # This is to run on c9.io.. you may need to change or make your own runner
    print "okta_config: {0}".format(config.okta)
    white_list_group_ids = []

    # Get all AD groups from Okta
    groups = get_ad_groups_from_okta()

    for group in groups:
        print "group type: {0} - object_class: {1} - name: {2}".format(group["type"], group["objectClass"], group["profile"]["name"])
        white_list_group_ids.append(group["id"])

    # White list selected groups in OIDC application
    print "Number of group ids to whitelist: {0}".format(len(white_list_group_ids))
    whitelist_app(white_list_group_ids)
