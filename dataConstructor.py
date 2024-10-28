
class DataConstructor():
    def __init__(self, filename) -> None:
        self.filename = filename
        self.team = self.get_team()
        self.players = self.get_players()

    def add_player(self, name, nb_licence):
        with open(self.filename, 'a') as file:
            file.write(name+";"+nb_licence+"\n")
        self.update()
    
    def change_presence(self, name):
        with open(self.filename, 'r') as file:
            lines = file.readlines()
        for i, line in enumerate(lines):
            if line.startswith(name):
                parts = line.strip().split(';')
                if parts[-1].strip() == 'true':
                    parts[-1] = 'false'
                else:
                    parts[-1] = 'true'
                lines[i] = ';'.join(parts) + '\n'

        with open(self.filename, 'w') as file:
            file.writelines(lines)
        self.update()

    def update(self):
        self.team = self.get_team()
        self.players = self.get_players()
    
    def get_team(self):
        with open(self.filename, 'r') as file:
            text = file.read()
        lines = text.splitlines(keepends=False)
        return lines[0] if lines else None
    
    def get_players(self):
        with open(self.filename, 'r') as file:
            text = file.read()
        lines = text.splitlines(keepends=False)
        return lines[1:]
    
    def show_player(self):
        players = []
        nb_licences = []
        is_present = []
        for player_line in self.players:
            player_line = player_line.split(sep=";")
            if len(player_line)>1:
                players.append(player_line[0])
                nb_licences.append(player_line[1])
                is_present.append(player_line[2]=='true')

        return self.team, players, nb_licences, is_present

