from giza.agents import GizaAgent


INFURA_URL = "https://sepolia.infura.io/v3/<infura-api-key>"

contracts = {
    'dao': '0xf247Cfa61a57FF361073b96Ce39BA051C485cA4A',
    'token_creation': '0x8df96034C1c7b2E1fe6E7751eD763a5755D5A4A7'
}

agent = GizaAgent(
        contracts=contracts,
        id=686,
        version_id=1,
        chain='ethereum:sepolia',
        account='first_account'
)

print("agent - ", agent)

with agent.execute() as contract:
    print(contract.dao.deployToken("My_Token", "TKEN", 10000, 1))
