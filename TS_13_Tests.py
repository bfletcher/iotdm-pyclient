import unittest
import iotdm_api

from onem2m_xml_protocols.ae import ae
from onem2m_xml_protocols.container import cnt
from onem2m_xml_protocols.contentinstance import cin
from onem2m_xml_protocols.subscription import sub
from onem2m_xml_protocols.remotecse import csr
from onem2m_xml_protocols.acp import acp, acr
from onem2m_xml_protocols.group import grp
from onem2m_xml_protocols.node import nod
from onem2m_xml_protocols.firmware import fwr


class TS13(unittest.TestCase):

    def test_TS13_Sequence(self):
    # Instantiate the api and start the reactor
        self.api = iotdm_api.Iotdm_api()
        self.api.start()
	
    # test_0_CSE_Provisioning
        print("test_0_CSE_Provisioning")
        (responseCode, responseString) = self.api.restConf('http://localhost', 'ODL-oneM2M-Cse', 'admin', 'admin')
        print("Result - Code: " + str(responseCode) + " String: " + responseString)

    # test_TD_M2M_NH_01_Retrieve_CSEBase
        print("test_TD_M2M_NH_01_Retrieve_CSEBase")
        (responseCode, responseString) = self.api.retrieve("coap://localhost:5683/ODL-oneM2M-Cse", origin="CSE3219/C9886", requestID="12345")
        print("Result - Code: " + str(responseCode) + " String: " + responseString)

    # test_TD_M2M_NH_06_Create_AE
        print("test_TD_M2M_NH_06_Create_AE")
        AE = ae()
        AE.set_api("Nk836-t071-fc022")
        AE.set_rr(True)
        AE.set_rn("TestAE")
        payload = AE.to_JSON()
        (responseCode, responseString) = self.api.create("coap://localhost:5683/ODL-oneM2M-Cse", 2, payload, origin="CSE3219/C9886", requestID="12345")
        print("Result - Code: " + str(responseCode) + " String: " + responseString)

    # test_TD_M2M_NH_07_Retrieve_AE
        print("test_TD_M2M_NH_07_Retrieve_AE")
        (responseCode, responseString) = self.api.retrieve("coap://localhost:5683/ODL-oneM2M-Cse/TestAE", origin="CSE3219/C9886", requestID="12345")
        print("Result - Code: " + str(responseCode) + " String: " + responseString)

    # test_TD_M2M_NH_08_Update_AE
        print("test_TD_M2M_NH_08_Update_AE - skipped")
    #    AE = ae()
    #    AE.set_acpi(["ODL-oneM2M-Cse/TestAE/TestACP"])
    #    payload = AE.to_JSON()
    #    (responseCode, responseString) = self.api.update("coap://localhost:5683/ODL-oneM2M-Cse/TestAE", payload, origin="admin", requestID="12345")

    # test_TD_M2M_NH_09_Delete_AE
        print("test_TD_M2M_NH_09_Delete_AE - skipped")
    #    (responseCode, responseString) = self.api.delete("coap://localhost:5683/ODL-oneM2M-Cse/TestAE", origin="CSE3219/C9886", requestID="12345")

    # test_TD_M2M_NH_10_Create_Container
        print("test_TD_M2M_NH_10_Create_Container")
        container = cnt()
        container.set_rn("TestContainer")
        payload = container.to_JSON()
        (responseCode, responseString) = self.api.create("coap://localhost:5683/ODL-oneM2M-Cse/TestAE", 3, payload, origin="CSE3219/C9886", requestID="12345")
        print("Result - Code: " + str(responseCode) + " String: " + responseString)

    # test_TD_M2M_NH_11_Retrieve_Container
        print("test_TD_M2M_NH_11_Retrieve_Container")
        (responseCode, responseString) = self.api.retrieve("coap://localhost:5683/ODL-oneM2M-Cse/TestAE/TestContainer", origin="CSE3219/C9886", requestID="12345")
        print("Result - Code: " + str(responseCode) + " String: " + responseString)

    # test_TD_M2M_NH_12_Update_Container
        print("test_TD_M2M_NH_12_Update_Container")
        container = cnt()
        payload = container.to_JSON()
        (responseCode, responseString) = self.api.update("coap://localhost:5683/ODL-oneM2M-Cse/TestAE/TestContainer", payload, origin="CSE3219/C9886", requestID="12345")
        print("Result - Code: " + str(responseCode) + " String: " + responseString)

    # test_TD_M2M_NH_13_Delete_Container
        print("test_TD_M2M_NH_13_Delete_Container - skipped")
    #    (responseCode, responseString) = self.api.delete("coap://localhost:5683/ODL-oneM2M-Cse/TestAE/TestContainer", origin="CSE3219/C9886", requestID="12345")

    # test_TD_M2M_NH_14_Create_ContentInstance
        print("test_TD_M2M_NH_14_Create_ContentInstance")
        con_instance = cin()
        con_instance.set_con("some data")
        con_instance.set_rn("TestContentInstance")
        payload = con_instance.to_JSON()
        (responseCode, responseString) = self.api.create("coap://localhost:5683/ODL-oneM2M-Cse/TestAE/TestContainer", 4, payload, origin="CSE3219/C9886", requestID="12345")
        print("Result - Code: " + str(responseCode) + " String: " + responseString)

    # test_TD_M2M_NH_15_Retrieve_ContentInstance
        print("test_TD_M2M_NH_15_Retrieve_ContentInstance")
        (responseCode, responseString) = self.api.retrieve("coap://localhost:5683/ODL-oneM2M-Cse/TestAE/TestContainer/TestContentInstance", origin="CSE3219/C9886", requestID="12345")
        print("Result - Code: " + str(responseCode) + " String: " + responseString)

    # test_TD_M2M_NH_17_Delete_ContentInstance
        print("test_TD_M2M_NH_17_Delete_ContentInstance - skipped")
    #    (responseCode, responseString) = self.api.delete("coap://localhost:5683/ODL-oneM2M-Cse/TestAE/TestContainer/TestContentInstance", origin="CSE3219/C9886", requestID="12345")
        print("Result - Code: " + str(responseCode) + " String: " + responseString)

    # test_TD_M2M_NH_18_Discovery_of_all_resources
        print("test_TD_M2M_NH_18_Discovery_of_all_resources")
        (responseCode, responseString) = self.api.retrieve("coap://localhost:5683/ODL-oneM2M-Cse?fu=1", origin="CSE3219/C9886", requestID="12345")
        print("Result - Code: " + str(responseCode) + " String: " + responseString)

    # test_TD_M2M_NH_19_Discovery_with_label_filter_criteria
        print("test_TD_M2M_NH_19_Discovery_with_label_filter_criteria")
        self.api.retrieve("coap://localhost:5683/ODL-oneM2M-Cse?fu=1&lbl=key1", origin="CSE3219/C9886", requestID="12345")
        print("Result - Code: " + str(responseCode) + " String: " + responseString)

    # test_TD_M2M_NH_20_Discovery_with_limit_filter_criteria
        print("test_TD_M2M_NH_20_Discovery_with_limit_filter_criteria")
        (responseCode, responseString) = self.api.retrieve("coap://localhost:5683/ODL-oneM2M-Cse?fu=1&lim=2", origin="CSE3219/C9886", requestID="12345")
        print("Result - Code: " + str(responseCode) + " String: " + responseString)

    # test_TD_M2M_NH_21_Discovery_with_multiple_filter_criteria
        print("test_TD_M2M_NH_21_Discovery_with_multiple_filter_criteria")
        (responseCode, responseString) = self.api.retrieve("coap://localhost:5683/ODL-oneM2M-Cse?fu=1&lbl=key1&lbl=key2", origin="CSE3219/C9886", requestID="12345")
        print("Result - Code: " + str(responseCode) + " String: " + responseString)

    # test_TD_M2M_NH_22_Create_Subscription
        print("test_TD_M2M_NH_22_Create_Subscription")
        subscription = sub()
        subscription.set_nu(["http://localhost"])
        subscription.set_rn("TestSubscription")
        payload = subscription.to_JSON()
        (responseCode, responseString) = self.api.create("coap://localhost:5683/ODL-oneM2M-Cse/TestAE/TestContainer", 23, payload, origin="CSE3219/C9886", requestID="12345")
        print("Result - Code: " + str(responseCode) + " String: " + responseString)

    # test_TD_M2M_NH_23_Retrieve_Subscription
        print("test_TD_M2M_NH_23_Retrieve_Subscription")
        (responseCode, responseString) = self.api.retrieve("coap://localhost:5683/ODL-oneM2M-Cse/TestAE/TestContainer/TestSubscription", origin="CSE3219/C9886", requestID="12345")
        print("Result - Code: " + str(responseCode) + " String: " + responseString)

    # test_TD_M2M_NH_24_Update_Subscription
        print("test_TD_M2M_NH_24_Update_Subscription")
        subscription = sub()
        payload = subscription.to_JSON()
        (responseCode, responseString) = self.api.update("coap://localhost:5683/ODL-oneM2M-Cse/TestAE/TestContainer/TestSubscription", payload, origin="CSE3219/C9886", requestID="12345")
        print("Result - Code: " + str(responseCode) + " String: " + responseString)

    # test_TD_M2M_NH_25_Delete_Subscription
        print("test_TD_M2M_NH_25_Delete_Subscription - skipped")
    #    (responseCode, responseString) = self.api.delete("coap://localhost:5683/ODL-oneM2M-Cse/TestAE/TestContainer/TestSubscription", origin="CSE3219/C9886", requestID="12345")

    # test_TD_M2M_NH_26_Create_AccessControlPolicy
        print("test_TD_M2M_NH_26_Create_AccessControlPolicy")
        accessControlRule1 = acr()
        accessControlRule1.set_acor(["*"])
        accessControlRule1.set_acop(63)
        pv_payload = accessControlRule1.to_JSON()
        accessControlRule2 = acr()
        accessControlRule2.set_acor(["admin"])
        accessControlRule2.set_acop(63)
        pvs_payload = accessControlRule2.to_JSON()
        accessControlPolicy = acp()
        accessControlPolicy.set_pv(pv_payload)
        accessControlPolicy.set_pvs(pvs_payload)
        accessControlPolicy.set_rn("TestACP")
        payload = accessControlPolicy.to_JSON()
        (responseCode, responseString) = self.api.create("coap://localhost:5683/ODL-oneM2M-Cse/TestAE", 1, payload, origin="CSE3219/C9886", requestID="12345")
        print("Result - Code: " + str(responseCode) + " String: " + responseString)

    # test_TD_M2M_NH_27_Retrieve_AccessControlPolicy
        print("test_TD_M2M_NH_27_Retrieve_AccessControlPolicy")
        (responseCode, responseString) = self.api.retrieve("coap://localhost:5683/ODL-oneM2M-Cse/TestAE/TestACP", origin="admin", requestID="12345")
        print("Result - Code: " + str(responseCode) + " String: " + responseString)

    # test_TD_M2M_NH_28_Update_AccessControlPolicy
        print("test_TD_M2M_NH_28_Update_AccessControlPolicy")
        accessControlRule1 = acr()
        accessControlRule1.set_acor(["admin"])
        accessControlRule1.set_acop(63)
        pv_payload = accessControlRule1.to_JSON()
        accessControlRule2 = acr()
        accessControlRule2.set_acor(["admin"])
        accessControlRule2.set_acop(63)
        pvs_payload = accessControlRule2.to_JSON()
        accessControlPolicy = acp()
        accessControlPolicy.set_pv(pv_payload)
        accessControlPolicy.set_pvs(pvs_payload)
        accessControlPolicy.set_rn("TestACP")
        payload = accessControlPolicy.to_JSON()
        (responseCode, responseString) = self.api.update("coap://localhost:5683/ODL-oneM2M-Cse/TestAE/TestACP", payload, origin="admin", requestID="12345")
        print("Result - Code: " + str(responseCode) + " String: " + responseString)

    # test_TD_M2M_NH_29_Delete_AccessControlPolicy
        print("test_TD_M2M_NH_29_Delete_AccessControlPolicy - skipped")
    #    (responseCode, responseString) = self.api.delete("coap://localhost:5683/ODL-oneM2M-Cse/TestAE/TestACP", origin="admin", requestID="12345")

    #Insufficient Access Rights
    # test_TD_M2M_NH_30_Unauthorized_operation
        print("test_TD_M2M_NH_30_Unauthorized_operation - skipped")
    #    (responseCode, responseString) = self.api.delete("coap://localhost:5683/ODL-oneM2M-Cse/TestAE/TestContainer", origin="CSE3219/C9886", requestID="12345")

    # test_TD_M2M_NH_31_Create_Group
        print("test_TD_M2M_NH_31_Create_Group")
        group = grp()
        group.set_mt(2)
        group.set_mnm(10)
        group.set_mid(["a"])
        group.set_rn("TestGroup")
        payload = group.to_JSON()
        (responseCode, responseString) = self.api.create("coap://localhost:5683/ODL-oneM2M-Cse", 9, payload, origin="CSE3219/C9886", requestID="12345")
        print("Result - Code: " + str(responseCode) + " String: " + responseString)

    # test_TD_M2M_NH_32_Retrieve_Group
        print("test_TD_M2M_NH_32_Retrieve_Group")
        (responseCode, responseString) = self.api.retrieve("coap://localhost:5683/ODL-oneM2M-Cse/TestGroup", origin="CSE3219/C9886", requestID="12345")
        print("Result - Code: " + str(responseCode) + " String: " + responseString)

    # test_TD_M2M_NH_33_Update_Group
        print("test_TD_M2M_NH_33_Update_Group")
        group = grp()
        payload = group.to_JSON()
        (responseCode, responseString) = self.api.update("coap://localhost:5683/ODL-oneM2M-Cse/TestGroup", payload, origin="CSE3219/C9886", requestID="12345")
        print("Result - Code: " + str(responseCode) + " String: " + responseString)

    # test_TD_M2M_NH_34_Delete_Group
        print("test_TD_M2M_NH_34_Delete_Group - skipped")
    #    (responseCode, responseString) = self.api.delete("coap://localhost:5683/ODL-oneM2M-Cse/TestGroup", origin="CSE3219/C9886", requestID="12345")

    # test_TD_M2M_NH_35_Create_Node
        print("test_TD_M2M_NH_35_Create_Node")
        node = nod()
        node.set_ni("a")
        node.set_rn("TestNode")
        payload = node.to_JSON()
        (responseCode, responseString) = self.api.create("coap://localhost:5683/ODL-oneM2M-Cse", 14, payload, origin="CSE3219/C9886", requestID="12345")
        print("Result - Code: " + str(responseCode) + " String: " + responseString)

    # test_TD_M2M_NH_36_Retrieve_Node
        print("test_TD_M2M_NH_36_Retrieve_Node")
        (responseCode, responseString) = self.api.retrieve("coap://localhost:5683/ODL-oneM2M-Cse/TestNode", origin="CSE3219/C9886", requestID="12345")
        print("Result - Code: " + str(responseCode) + " String: " + responseString)

    # test_TD_M2M_NH_37_Update_Node
        print("test_TD_M2M_NH_37_Update_Node")
        node = nod()
        payload = node.to_JSON()
        (responseCode, responseString) = self.api.update("coap://localhost:5683/ODL-oneM2M-Cse/TestNode", payload, origin="CSE3219/C9886", requestID="12345")
        print("Result - Code: " + str(responseCode) + " String: " + responseString)

    # test_TD_M2M_NH_38_Delete_Node
        print("test_TD_M2M_NH_38_Delete_Node - skipped")
    #    (responseCode, responseString) = self.api.delete("coap://localhost:5683/ODL-oneM2M-Cse/TestNode", origin="CSE3219/C9886", requestID="12345")

    # Stop the reactor
        self.api.stop()



if __name__ == '__main__':
    unittest.main()
