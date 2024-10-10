from datetime import datetime, timedelta

def main(event):
  tsdate = int(event.get("inputFields").get("tsdate"))
  tsdate = tsdate / 1000
  tsdate = datetime.utcfromtimestamp(tsdate)
  tedate = tsdate + timedelta(days = 30)
  tedate = int(tedate.timestamp() * 1000)
  return {
    "outputFields": {
      "transitionenddate": tedate
    }
  }