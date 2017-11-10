import time
import logging as lg

def testFun():
    lgr.error("this is testFun")

lg.basicConfig(level=lg.INFO)
lgr=lg.getLogger(__name__)
# + time.strftime('%d/%m/%Y_%H%M%S') + ".txt"

hdlr = lg.FileHandler(r"logs\log.txt")
hdlr.setLevel(level=lg.INFO)

frmt=lg.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
hdlr.setFormatter(frmt)

lgr.addHandler(hdlr)

lgr.info("this is info")
lgr.warning("this is warn")
lgr.error("this is error")

testFun()
