import xml.dom.minidom
from datetime import datetime
import xml.sax

#DOM
def run_dom_analysis():
    print("\nRunning DOM analysis...")
    start_time = datetime.now()

    # Parse the XML file
    DOMTree = xml.dom.minidom.parse("go_obo.xml")
    collection = DOMTree.documentElement
    
    # Initialize counters
    max_counts = {
    "biological_process": {"count": 0, "terms_id": []},
    "molecular_function": {"count": 0, "terms_id": []},
    "cellular_component": {"count": 0, "terms_id": []}
    }
            
    # Process each term
    terms = collection.getElementsByTagName('term')
    for term in terms:
        namespace = term.getElementsByTagName('namespace')[0].firstChild.nodeValue
        is_a_count = len(term.getElementsByTagName('is_a'))
        if is_a_count > max_counts[namespace]["count"]:
           
            # Initialize counters
            max_counts[namespace]["count"] = 0
            max_counts[namespace]["terms_id"] = []
            
            # Update max counts
            max_counts[namespace]["count"] = is_a_count
            max_counts[namespace]["terms_id"].append(term.getElementsByTagName('id')[0].firstChild.nodeValue)
            
        elif is_a_count == max_counts[namespace]["count"]:
            max_counts[namespace]["terms_id"].append(term.getElementsByTagName('id')[0].firstChild.nodeValue)
            
    # Print results
    for namespace, data in max_counts.items():
        print(f"{namespace} (max is_a count: {data['count']})\nid: {data['terms_id']}")
        
    end_time = datetime.now()
    print(f"DOM analysis completed in: {end_time - start_time}")

run_dom_analysis()



#SAX
class GOHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.current_data = ""
        self.current_namespace = ""
        self.current_id = ""
        self.is_a_count = 0
        self.max_counts = {
            "biological_process": {"count": 0, "terms_id": []},
            "molecular_function": {"count": 0, "terms_id": []},
            "cellular_component": {"count": 0, "terms_id": []}
        }
       
    def startElement(self, tag, attributes):
        self.current_data = tag
        if tag == "term":
            self.is_a_count = 0
            self.current_namespace = ""
            self.current_id = ""
        elif tag == "is_a":
            self.is_a_count += 1
    
    def characters(self, content):
        if self.current_data == "namespace":
            self.current_namespace += content.strip()
        elif self.current_data == "id":
            self.current_id += content.strip()
    
    def endElement(self, tag):
        if tag == "term":
            if self.current_namespace in self.max_counts:
                namespace_data = self.max_counts[self.current_namespace]
                if self.is_a_count > namespace_data["count"]:
                    namespace_data["count"] = self.is_a_count
                    namespace_data["terms_id"] = [self.current_id]
                elif self.is_a_count == namespace_data["count"]:
                    namespace_data["terms_id"].append(self.current_id)


def run_sax_analysis():
    print("\nRunning SAX analysis...")
    start_time = datetime.now()
    
    parser = xml.sax.make_parser()
    handler = GOHandler()
    parser.setContentHandler(handler)
    parser.parse("go_obo.xml")

    # Print results
    for namespace, data in handler.max_counts.items():
        print(f"{namespace} (max is_a count: {data['count']})\nid: {data['terms_id']}")
        
    end_time = datetime.now()
    print(f"SAX analysis completed in: {end_time - start_time}")

run_sax_analysis()


# SAX run faster than DOM !!




