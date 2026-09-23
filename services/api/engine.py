
from common import Store, chain_ok
import json
SEED={"en-US":["Name the local river.","Count market stalls."],"es-US":["Nombra el rio local.","Cuenta los puestos."]}
def mismatch(answer, locale):
    keys=locale.lower().split("-")+["river","rio","market","puesto","local"]
    return not any(k in answer.lower() for k in keys)
class Core:
    def __init__(self, db): self.s=Store(db)
    def compose(self, learner, locale, topic):
        return self.s.append("cur.compose", {"learner":learner,"locale":locale,"topic":topic,"items":SEED.get(locale,SEED["en-US"]),"gen":1})
    def score(self, learner, answers):
        last=[json.loads(r["body"]) for r in self.s.list("cur.compose") if json.loads(r["body"])["learner"]==learner][-1]
        hits=sum(1 for a in answers if not mismatch(a,last["locale"]))
        plateau = hits==0 or all(len(a)<8 for a in answers)
        return self.s.append("cur.score", {"learner":learner,"hits":hits,"plateau":plateau,"mismatch":hits<len(answers)})
    def evolve(self, learner):
        scores=[json.loads(r["body"]) for r in self.s.list("cur.score") if json.loads(r["body"])["learner"]==learner]
        if not scores: raise ValueError("no scores")
        last=scores[-1]
        pedagogy="scaffold-local" if last["plateau"] or last["mismatch"] else "stretch"
        items=["Describe one street you walk."] if pedagogy=="scaffold-local" else ["Compare two harvest seasons."]
        return self.s.append("cur.evolve", {"learner":learner,"pedagogy":pedagogy,"items":items})
    def proof(self):
        self.compose("ju","es-US","market"); self.score("ju",["hello","xyz"]); ev=self.evolve("ju")
        return {"ok":chain_ok(self.s),"evolved":ev}
