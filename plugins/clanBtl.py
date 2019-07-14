from nonebot import on_command, CommandSession
from nonebot.permission import GROUP, PRIVATE_FRIEND
import re
import csv

@on_command('askBoss', aliases=('查boss', '查Boss', '查BOSS'), permission=GROUP | PRIVATE_FRIEND, only_to_me=True)
async def askBoss(session: CommandSession):
	bossName = session.state['bossName'] if 'bossName' in session.state else None
	if not bossName:
		bossName = session.get('bossName', prompt='输入想要查询的boss，阶段数和编号用半角数字')
	bossLocStr = re.findall('[0-9]', bossName)
	if len(bossLocStr) != 2:
		await session.send('guna!')
		return
	bossLoc = [int(bossLocStr[0]), int(bossLocStr[1])]
	bossIndex = 5*(bossLoc[0]-1)+bossLoc[1]-1
	if bossLoc[0]>3 or bossLoc[1]>5:
		await session.send('guna!')
		return
	#bossInfo = open('C:/Users/chrysalis/OneDrive/clanbtl/plugins/boss.csv', 'r')
	bossInfo = open('./plugins/boss.csv', 'r')
	reader = csv.reader(bossInfo)
	for i, rows in enumerate(reader):
		if i == bossIndex:
			row = rows
	bossAns = bossLocStr[0]+'阶段'+bossLocStr[1]+'号：'+'物理防御'+row[2]+'，魔法防御'+row[3]
	bossInfo.close()
	await session.send(bossAns)
	
@askBoss.args_parser
async def _(session:CommandSession):
	stripped_arg = session.current_arg_text.strip()
	if session.is_first_run:
		if stripped_arg:
			session.state['bossName'] = stripped_arg
		return
		
	if not stripped_arg:
		session.pause('输入想要查询的boss，阶段数和编号用半角数字')
		
	session.state[session.current_key] = stripped_arg