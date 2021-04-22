class Solution(object):
    def dayOfYear(self, date):
        """
        :type date: str
        :rtype: int
        """
        day = int(date.split("-")[2])
        month = int(date.split("-")[1])
        year = int(date.split("-")[0])
        days_normal = [31,28,31,30,31,30,31,31,30,31,30,31]
        days_leap = [31,29,31,30,31,30,31,31,30,31,30,31]
        leap = ""
        if year % 4 == 0:
            if year % 100 == 0:
                if year % 400 == 0:
                    leap = "yes"
            else:
                leap = "yes"
        else:
            leap = "no"
        day_of_year = 0 
        if leap == "yes":
            for i in range(month):
                if i+1 != month:
                    day_of_year += days_leap[i]
                else:
                    day_of_year += day
            return day_of_year
        else:
            for i in range(month):
                if i+1 != month:
                    day_of_year += days_normal[i]
                else:
                    day_of_year += day
            return day_of_year
                    
        