import fitz

class pdfWriter():
    def __init__(self, pdfPath):
        self.pdfPath = pdfPath
        self.doc = fitz.open(self.pdfPath)
    
    def write(self, team, players, nb_licences, is_present):
        if len(players) != len(nb_licences):
            raise ValueError("Player and license lists must have the same length.")

        page = self.doc[0] 

        # Team name
        font_size = 15
        x, y = 38, 148
        page.insert_text((x, y), team, fontsize=font_size, fontname="helv", color=(0, 0, 0))
        
        font_size = 10
        i = 0
        for (player, nb_licence, is_pres) in zip(players, nb_licences, is_present):
            if is_pres and i<16:
                x, y = 72, 243 + i * 25.5
                page.insert_text((x, y), player, fontsize=font_size, fontname="helv", color=(0, 0, 0))
                page.insert_text((x + 170, y), nb_licence, fontsize=font_size, fontname="helv", color=(0, 0, 0))
                i += 1

    def save(self, save_path):
        self.doc.save(save_path)
        self.doc.close()