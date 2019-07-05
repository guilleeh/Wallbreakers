from collections import defaultdict


class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        domain_dict = defaultdict(int)
        result = []
        for domain in cpdomains:
            count_and_subdomain = domain.split(" ")
            subdomains = count_and_subdomain[1].split(".")
            count = count_and_subdomain[0]
            domain_string = ""
            start = True
            for sub in subdomains[::-1]:
                if start:
                    domain_string += sub
                    start = False
                else:
                    domain_string = sub + "." + domain_string
                domain_dict[domain_string] += int(count)

        for key, value in domain_dict.items():
            result.append(str(value) + " " + key)

        return result
