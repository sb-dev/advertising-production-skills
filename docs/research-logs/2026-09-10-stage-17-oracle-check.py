"""Exact arithmetic for Stage 17 synthetic design, not an installed-agent eval."""
from fractions import Fraction
import json

def run():
    checks=[]
    def check(name, actual, expected):
        if actual != expected:
            raise AssertionError(f'{name}: {actual!r} != {expected!r}')
        checks.append({'check':name,'result':'PASS'})
    check('K refund A',Fraction(20,100),Fraction(1,5))
    check('K refund B',Fraction(10,100),Fraction(1,10))
    check('K retained cost A',Fraction(600,40),15)
    check('K retained cost B',Fraction(600,50),12)
    check('K contribution A',40*8-600,-280)
    check('K contribution B',50*8-600,-200)
    cohorts=[('C1',60,10,3,1,1),('C2',45,10,2,1,0),('C3',15,10,3,0,0),('C4',5,10,1,0,0)]
    check('F contacts',sum(c[2] for c in cohorts),40)
    check('F qualified',sum(c[3] for c in cohorts),9)
    check('F signed cohort outcomes',sum(c[4] for c in cohorts),2)
    check('F delivered cohort outcomes',sum(c[5] for c in cohorts),1)
    commitments={'C2':8,'B0':8}
    check('F upcoming committed hours',sum(commitments.values()),16)
    check('F remaining slots',(16-sum(commitments.values()))//8,0)
    check('F lead-entry maturity',[c[0] for c in cohorts if c[1]>=45],['C1','C2'])
    check('F completed C1 not booked again','C1' not in commitments,True)
    check('F B0 outside reported cohort population','B0' not in [c[0] for c in cohorts],True)
    check('E verified per attempt',Fraction(12,20),Fraction(3,5))
    check('E useful per verified installation',Fraction(8,12),Fraction(2,3))
    check('Negative: double-subtracted K refunds rejected',Fraction(600,40-20)!=15,True)
    check('Negative: third FDE slot rejected',3*8>16,True)
    check('Negative: visitor ratio is not installation ratio',Fraction(8,100)!=Fraction(8,12),True)
    return {'scope':'synthetic arithmetic and fixture consistency only','checks':checks,'count':len(checks),'negative_checks':3}

if __name__=='__main__':
    print(json.dumps(run(),indent=2))
