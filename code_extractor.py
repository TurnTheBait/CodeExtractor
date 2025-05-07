import os
from tkinter import Tk, filedialog, Button, Label, Frame
from tkinter.messagebox import showinfo


# Funzione per ottenere tutti i file dalla cartella selezionata e dalle sottocartelle
def get_files_in_directory(directory):
    """Ottiene tutti i file (non le cartelle) dalla cartella e dalle sottocartelle."""
    files = []
    for root, dirs, filenames in os.walk(directory):  # 'os.walk' esplora tutte le sottocartelle
        for filename in filenames:
            # Aggiunge il percorso completo del file alla lista
            files.append(os.path.join(root, filename))
    return files


# Funzione per scrivere il codice in un file di testo
def write_code_to_file(files, output_path):
    """Scrive il codice di tutti i file in un file di testo."""
    with open(output_path, 'w', encoding='utf-8') as f_out:
        for file in files:
            # Aggiungiamo un commento con il nome del file
            file_name = os.path.basename(file)
            f_out.write(f"#################### File: {file_name} ####################\n")

            try:
                # Leggiamo il contenuto del file
                with open(file, 'r', encoding='utf-8') as f_in:
                    f_out.write(f_in.read())
            except UnicodeDecodeError:
                # In caso di errore nella lettura (file binario, ecc.), saltiamo il file
                f_out.write(f"\n# Errore nella lettura del file: {file_name}\n")

            # Aggiungiamo una separazione tra i file
            f_out.write("\n\n")


# Funzione per la selezione della cartella
def select_directory():
    """Permette all'utente di selezionare una cartella."""
    folder_selected = filedialog.askdirectory()
    if folder_selected:
        # Troviamo tutti i file nella cartella selezionata
        files = get_files_in_directory(folder_selected)
        if not files:
            showinfo("Nessun file trovato", "La cartella selezionata non contiene file di codice.")
        else:
            # Chiediamo dove salvare il file di output
            output_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
            if output_path:
                write_code_to_file(files, output_path)
                showinfo("Operazione completata", f"Il file di testo è stato salvato in: {output_path}")
            else:
                showinfo("Operazione annullata", "Non è stato selezionato un percorso di salvataggio.")


# Funzione per creare l'interfaccia grafica
def create_gui():
    """Crea l'interfaccia grafica."""
    root = Tk()
    root.title("Generatore di Codice da Cartella")
    root.geometry("400x250")
    root.configure(bg='#f0f0f0')  # Impostiamo uno sfondo chiaro

    # Frame principale
    frame = Frame(root, bg='#f0f0f0')
    frame.pack(pady=30)

    # Titolo
    label = Label(frame, text="Generatore di Codice", font=("Helvetica", 16), bg='#f0f0f0')
    label.pack(pady=10)

    # Descrizione
    description = Label(frame, text="Seleziona una cartella per generare il file .txt", font=("Helvetica", 12),
                        bg='#f0f0f0')
    description.pack(pady=5)

    # Pulsante per selezionare la cartella
    button = Button(frame, text="Seleziona Cartella", command=select_directory, font=("Helvetica", 12), bg='#4CAF50',
                    fg='white', relief="solid", width=20)
    button.pack(pady=15)

    # Avvio dell'interfaccia grafica
    root.mainloop()


# Esecuzione dell'app
if __name__ == "__main__":
    create_gui()
