"""
Munim's Dictionary
A single-file English-Bengali dictionary built with Tkinter.

Install dependencies:
    python -m pip install pyttsx3 gTTS pygame

English speech: pyttsx3 (usually works offline if a suitable system voice exists).
Bengali speech: gTTS (requires an internet connection), played with pygame.
"""

import threading
import tkinter as tk
from tkinter import ttk, messagebox
import tempfile
import os

# English word -> Bengali meaning. Exactly 200 entries, displayed alphabetically.
DICTIONARY = {
    "Ability": "ক্ষমতা",
    "About": "সম্পর্কে",
    "Above": "উপরে",
    "Accept": "গ্রহণ করা",
    "Action": "কাজ",
    "Active": "সক্রিয়",
    "Advice": "পরামর্শ",
    "Afraid": "ভীত",
    "After": "পরে",
    "Again": "আবার",
    "Age": "বয়স",
    "Air": "বাতাস",
    "Always": "সবসময়",
    "Amazing": "অসাধারণ",
    "Animal": "প্রাণী",
    "Answer": "উত্তর",
    "Apple": "আপেল",
    "Application": "অ্যাপ্লিকেশন",
    "Area": "এলাকা",
    "Arrange": "সাজানো",
    "Artificial": "কৃত্রিম",
    "Ask": "জিজ্ঞাসা করা",
    "Attention": "মনোযোগ",
    "Available": "উপলভ্য",
    "Beautiful": "সুন্দর",
    "Because": "কারণ",
    "Become": "হয়ে ওঠা",
    "Begin": "শুরু করা",
    "Believe": "বিশ্বাস করা",
    "Best": "সেরা",
    "Better": "আরও ভালো",
    "Book": "বই",
    "Brave": "সাহসী",
    "Bright": "উজ্জ্বল",
    "Build": "তৈরি করা",
    "Business": "ব্যবসা",
    "Calm": "শান্ত",
    "Care": "যত্ন",
    "Careful": "সতর্ক",
    "Carry": "বহন করা",
    "Change": "পরিবর্তন",
    "Character": "চরিত্র",
    "Child": "শিশু",
    "Choose": "বেছে নেওয়া",
    "City": "শহর",
    "Clean": "পরিষ্কার",
    "Clever": "চতুর",
    "Cloud": "মেঘ",
    "Code": "কোড",
    "Communication": "যোগাযোগ",
    "Computer": "কম্পিউটার",
    "Confidence": "আত্মবিশ্বাস",
    "Create": "তৈরি করা",
    "Creative": "সৃজনশীল",
    "Culture": "সংস্কৃতি",
    "Curious": "কৌতূহলী",
    "Daily": "দৈনিক",
    "Danger": "বিপদ",
    "Data": "তথ্য",
    "Decision": "সিদ্ধান্ত",
    "Deep": "গভীর",
    "Develop": "উন্নয়ন করা",
    "Dictionary": "অভিধান",
    "Different": "ভিন্ন",
    "Difficult": "কঠিন",
    "Digital": "ডিজিটাল",
    "Dream": "স্বপ্ন",
    "Early": "আগে",
    "Earth": "পৃথিবী",
    "Education": "শিক্ষা",
    "Effort": "প্রচেষ্টা",
    "Emotion": "আবেগ",
    "Energy": "শক্তি",
    "Enjoy": "উপভোগ করা",
    "Enough": "যথেষ্ট",
    "Environment": "পরিবেশ",
    "Error": "ভুল",
    "Example": "উদাহরণ",
    "Experience": "অভিজ্ঞতা",
    "Explain": "ব্যাখ্যা করা",
    "Family": "পরিবার",
    "Famous": "বিখ্যাত",
    "Fast": "দ্রুত",
    "Fear": "ভয়",
    "Feel": "অনুভব করা",
    "Friend": "বন্ধু",
    "Future": "ভবিষ্যৎ",
    "Game": "খেলা",
    "Garden": "বাগান",
    "Gentle": "নম্র",
    "Gift": "উপহার",
    "Give": "দেওয়া",
    "Goal": "লক্ষ্য",
    "Good": "ভালো",
    "Government": "সরকার",
    "Grow": "বেড়ে ওঠা",
    "Happy": "সুখী",
    "Health": "স্বাস্থ্য",
    "Help": "সাহায্য",
    "History": "ইতিহাস",
    "Honest": "সৎ",
    "Hope": "আশা",
    "Idea": "ধারণা",
    "Important": "গুরুত্বপূর্ণ",
    "Improve": "উন্নত করা",
    "Information": "তথ্য",
    "Innovation": "উদ্ভাবন",
    "Inspire": "অনুপ্রাণিত করা",
    "Intelligent": "বুদ্ধিমান",
    "Internet": "ইন্টারনেট",
    "Knowledge": "জ্ঞান",
    "Language": "ভাষা",
    "Learn": "শেখা",
    "Library": "গ্রন্থাগার",
    "Life": "জীবন",
    "Listen": "শোনা",
    "Love": "ভালোবাসা",
    "Machine": "যন্ত্র",
    "Manage": "পরিচালনা করা",
    "Meaning": "অর্থ",
    "Memory": "স্মৃতি",
    "Mind": "মন",
    "Mobile": "মুঠোফোন",
    "Modern": "আধুনিক",
    "Motivation": "অনুপ্রেরণা",
    "Music": "সংগীত",
    "Nature": "প্রকৃতি",
    "Necessary": "প্রয়োজনীয়",
    "Network": "নেটওয়ার্ক",
    "New": "নতুন",
    "News": "খবর",
    "Opportunity": "সুযোগ",
    "Organize": "গুছিয়ে রাখা",
    "Peace": "শান্তি",
    "People": "মানুষ",
    "Perfect": "নিখুঁত",
    "Plan": "পরিকল্পনা",
    "Plant": "উদ্ভিদ",
    "Play": "খেলা",
    "Positive": "ইতিবাচক",
    "Practice": "অনুশীলন",
    "Problem": "সমস্যা",
    "Program": "প্রোগ্রাম",
    "Programming": "প্রোগ্রামিং",
    "Progress": "অগ্রগতি",
    "Protect": "রক্ষা করা",
    "Quality": "গুণমান",
    "Question": "প্রশ্ন",
    "Quick": "দ্রুত",
    "Quiet": "নীরব",
    "Reason": "কারণ",
    "Remember": "মনে রাখা",
    "Respect": "সম্মান",
    "Result": "ফলাফল",
    "River": "নদী",
    "Safe": "নিরাপদ",
    "Science": "বিজ্ঞান",
    "Search": "খোঁজা",
    "Share": "ভাগ করে নেওয়া",
    "Skill": "দক্ষতা",
    "Smart": "চালাক",
    "Smile": "হাসি",
    "Software": "সফটওয়্যার",
    "Solution": "সমাধান",
    "Speak": "কথা বলা",
    "Strong": "শক্তিশালী",
    "Study": "পড়াশোনা",
    "Success": "সাফল্য",
    "Support": "সহায়তা",
    "System": "ব্যবস্থা",
    "Talent": "প্রতিভা",
    "Teacher": "শিক্ষক",
    "Team": "দল",
    "Technology": "প্রযুক্তি",
    "Think": "চিন্তা করা",
    "Time": "সময়",
    "Together": "একসঙ্গে",
    "Travel": "ভ্রমণ",
    "Trust": "বিশ্বাস",
    "Understand": "বোঝা",
    "Unique": "অনন্য",
    "University": "বিশ্ববিদ্যালয়",
    "Useful": "উপকারী",
    "Value": "মূল্য",
    "Victory": "বিজয়",
    "Voice": "কণ্ঠস্বর",
    "Wait": "অপেক্ষা করা",
    "Warm": "উষ্ণ",
    "Water": "পানি",
    "Wealth": "সম্পদ",
    "Welcome": "স্বাগতম",
    "Wisdom": "প্রজ্ঞা",
    "Wise": "জ্ঞানী",
    "Work": "কাজ",
    "World": "পৃথিবী",
    "Write": "লেখা",
    "Young": "তরুণ",
    "Youth": "যৌবন",
    "Zeal": "উৎসাহ",
    "Zero": "শূন্য",
}

# Keep the search and suggestion ordering deterministic.
WORDS = sorted(DICTIONARY, key=str.casefold)


class MunimsDictionary:
    def __init__(self, root):
        self.root = root
        self.root.title("Munim's Dictionary")
        self.root.geometry("760x600")
        self.root.minsize(600, 500)
        self.root.configure(bg="#f3f6fb")

        self.current_word = None
        self.speech_lock = threading.Lock()
        self.stop_event = threading.Event()
        self.tts_engine = None
        self.tts_engine_lock = threading.Lock()
        self.pygame_mixer_ready = False
        self.bangla_audio_path = None

        self._configure_style()
        self._build_ui()
        self.root.protocol("WM_DELETE_WINDOW", self.close_app)

    def _configure_style(self):
        style = ttk.Style()
        try:
            style.theme_use("clam")
        except tk.TclError:
            pass
        style.configure(
            "TButton",
            font=("Segoe UI", 10),
            padding=(12, 8),
        )
        style.configure(
            "Primary.TButton",
            font=("Segoe UI", 10, "bold"),
            padding=(16, 9),
        )
        style.configure(
            "TEntry",
            font=("Segoe UI", 12),
            padding=8,
        )

    def _build_ui(self):
        main = tk.Frame(self.root, bg="#f3f6fb", padx=28, pady=24)
        main.pack(fill="both", expand=True)

        header = tk.Frame(main, bg="#f3f6fb")
        header.pack(fill="x", pady=(0, 22))

        tk.Label(
            header,
            text="Munim's Dictionary",
            font=("Segoe UI", 25, "bold"),
            fg="#173b67",
            bg="#f3f6fb",
        ).pack(anchor="w")

        tk.Label(
            header,
            text="English words with Bengali meanings",
            font=("Segoe UI", 11),
            fg="#61738a",
            bg="#f3f6fb",
        ).pack(anchor="w", pady=(4, 0))

        search_card = tk.Frame(
            main, bg="white", padx=18, pady=18,
            highlightbackground="#dce4ef", highlightthickness=1,
        )
        search_card.pack(fill="x")

        tk.Label(
            search_card,
            text="Search for a word",
            font=("Segoe UI", 11, "bold"),
            fg="#263b53",
            bg="white",
        ).pack(anchor="w", pady=(0, 8))

        search_row = tk.Frame(search_card, bg="white")
        search_row.pack(fill="x")

        self.search_var = tk.StringVar()
        self.search_entry = ttk.Entry(search_row, textvariable=self.search_var)
        self.search_entry.pack(side="left", fill="x", expand=True)
        self.search_entry.insert(0, "Enter word name")
        self.search_entry.configure(foreground="#888888")
        self.search_entry.bind("<FocusIn>", self._clear_placeholder)
        self.search_entry.bind("<FocusOut>", self._restore_placeholder)
        self.search_entry.bind("<KeyRelease>", self._update_suggestions)
        self.search_entry.bind("<Down>", self._focus_suggestions)
        self.search_entry.bind("<Return>", self.show_meaning)
        self.search_entry.bind("<Escape>", self._hide_suggestions)

        self.show_button = ttk.Button(
            search_row, text="Show", style="Primary.TButton",
            command=self.show_meaning,
        )
        self.show_button.pack(side="left", padx=(10, 0))

        self.suggestion_box = tk.Listbox(
            search_card,
            height=5,
            font=("Segoe UI", 11),
            activestyle="dotbox",
            selectbackground="#d8e9ff",
            selectforeground="#173b67",
            bg="white",
            fg="#263b53",
            relief="solid",
            borderwidth=1,
            highlightthickness=0,
        )
        self.suggestion_box.bind("<<ListboxSelect>>", self._select_suggestion)
        self.suggestion_box.bind("<Return>", self._accept_suggestion)
        self.suggestion_box.bind("<Double-Button-1>", self._accept_suggestion)
        self.suggestion_box.bind("<Escape>", self._hide_suggestions)

        result_card = tk.Frame(
            main, bg="white", padx=22, pady=20,
            highlightbackground="#dce4ef", highlightthickness=1,
        )
        result_card.pack(fill="both", expand=True, pady=(18, 0))

        tk.Label(
            result_card,
            text="Dictionary Result",
            font=("Segoe UI", 11, "bold"),
            fg="#61738a",
            bg="white",
        ).pack(anchor="w")

        self.word_label = tk.Label(
            result_card,
            text="Search for an English word",
            font=("Segoe UI", 20, "bold"),
            fg="#173b67",
            bg="white",
            anchor="w",
            wraplength=650,
        )
        self.word_label.pack(fill="x", pady=(15, 5))

        self.meaning_label = tk.Label(
            result_card,
            text="বাংলা অর্থ এখানে দেখা যাবে",
            font=("Nirmala UI", 19),
            fg="#176b55",
            bg="white",
            anchor="w",
            justify="left",
            wraplength=650,
        )
        self.meaning_label.pack(fill="x", pady=(0, 20))

        voice_row = tk.Frame(result_card, bg="white")
        voice_row.pack(anchor="w", fill="x")

        self.english_button = ttk.Button(
            voice_row, text="🔊 Speak English",
            command=self.speak_english,
        )
        self.english_button.pack(side="left", padx=(0, 8), pady=(0, 8))

        self.bangla_button = ttk.Button(
            voice_row, text="🔊 Speak Bangla",
            command=self.speak_bangla,
        )
        self.bangla_button.pack(side="left", padx=(0, 8), pady=(0, 8))

        self.stop_button = ttk.Button(
            voice_row, text="■ Stop Voice",
            command=self.stop_voice,
        )
        self.stop_button.pack(side="left", pady=(0, 8))

        self.status_var = tk.StringVar(value="Ready")
        tk.Label(
            main,
            textvariable=self.status_var,
            font=("Segoe UI", 9),
            fg="#61738a",
            bg="#f3f6fb",
            anchor="w",
        ).pack(fill="x", pady=(10, 0))

        self.search_entry.focus_set()

    def _clear_placeholder(self, _event=None):
        if self.search_entry.get() == "Enter word name":
            self.search_entry.delete(0, tk.END)
            self.search_entry.configure(foreground="#263b53")

    def _restore_placeholder(self, _event=None):
        if not self.search_entry.get().strip():
            self.search_entry.insert(0, "Enter word name")
            self.search_entry.configure(foreground="#888888")
            self._hide_suggestions()

    def _update_suggestions(self, event=None):
        if event and event.keysym in ("Up", "Down", "Return", "Escape"):
            return

        query = self.search_var.get().strip()
        if query == "Enter word name" or not query:
            self._hide_suggestions()
            return

        matches = [word for word in WORDS if word.casefold().startswith(query.casefold())]
        if not matches:
            # If no prefix match, offer words containing the typed text.
            matches = [word for word in WORDS if query.casefold() in word.casefold()]

        self.suggestion_box.delete(0, tk.END)
        for word in matches[:8]:
            self.suggestion_box.insert(tk.END, word)

        if matches:
            self.suggestion_box.pack(fill="x", pady=(8, 0))
        else:
            self.suggestion_box.pack_forget()

    def _hide_suggestions(self, _event=None):
        self.suggestion_box.pack_forget()
        return "break"

    def _focus_suggestions(self, _event=None):
        if self.suggestion_box.winfo_ismapped() and self.suggestion_box.size():
            self.suggestion_box.focus_set()
            self.suggestion_box.selection_clear(0, tk.END)
            self.suggestion_box.selection_set(0)
            self.suggestion_box.activate(0)
            return "break"

    def _select_suggestion(self, _event=None):
        selection = self.suggestion_box.curselection()
        if selection:
            word = self.suggestion_box.get(selection[0])
            self.search_var.set(word)

    def _accept_suggestion(self, _event=None):
        self._select_suggestion()
        self._hide_suggestions()
        self.search_entry.focus_set()
        self.show_meaning()
        return "break"

    def show_meaning(self, _event=None):
        word = self.search_var.get().strip()
        if not word or word == "Enter word name":
            messagebox.showinfo("Search required", "Please enter an English word.")
            self.search_entry.focus_set()
            return "break"

        found = next((key for key in DICTIONARY if key.casefold() == word.casefold()), None)
        if found is None:
            self.current_word = None
            self.word_label.configure(text=word)
            self.meaning_label.configure(text="অর্থ পাওয়া যায়নি  |  Meaning not found")
            self.status_var.set("This word is not in the built-in dictionary.")
        else:
            self.current_word = found
            self.search_var.set(found)
            self.word_label.configure(text=found)
            self.meaning_label.configure(text=DICTIONARY[found])
            self.status_var.set("Meaning found.")
        self._hide_suggestions()
        self.search_entry.focus_set()
        return "break"

    def _get_current_entry(self):
        if self.current_word and self.current_word in DICTIONARY:
            return self.current_word, DICTIONARY[self.current_word]

        query = self.search_var.get().strip()
        found = next((key for key in DICTIONARY if key.casefold() == query.casefold()), None)
        if found:
            self.current_word = found
            return found, DICTIONARY[found]

        messagebox.showinfo("No word selected", "Search for a word and click Show first.")
        return None, None

    def speak_english(self):
        word, _meaning = self._get_current_entry()
        if not word:
            return
        self.stop_event.clear()
        threading.Thread(
            target=self._english_speech_worker, args=(word,), daemon=True
        ).start()

    def _english_speech_worker(self, word):
        engine = None
        try:
            import pyttsx3

            # Serialize speech requests and create a fresh Windows SAPI5
            # engine each time to avoid "run loop already started".
            with self.speech_lock:
                if self.stop_event.is_set():
                    return

                engine = pyttsx3.init("sapi5")
                self.tts_engine = engine

                # Prefer an English voice if one is installed in Windows.
                try:
                    voices = engine.getProperty("voices")
                    for voice in voices:
                        details = (
                            str(getattr(voice, "id", "")) + " " +
                            str(getattr(voice, "name", ""))
                        ).lower()
                        if "english" in details or "en_" in details or "en-" in details:
                            engine.setProperty("voice", voice.id)
                            break
                except Exception:
                    pass

                if self.stop_event.is_set():
                    engine.stop()
                    return

                engine.say(word)
                engine.runAndWait()

            if not self.stop_event.is_set():
                self._set_status("Finished speaking English.")
        except ImportError as exc:
            self._show_error(
                "English voice import error",
                f"Python could not import pyttsx3.\nDetails: {exc}\n\n"
                "Run: python -m pip install pyttsx3",
            )
        except Exception as exc:
            if not self.stop_event.is_set():
                self._show_error(
                    "English voice unavailable",
                    f"Could not speak the English word.\n\nDetails: {exc}",
                )
        finally:
            if engine is not None:
                try:
                    engine.stop()
                except Exception:
                    pass
            if self.tts_engine is engine:
                self.tts_engine = None

    def speak_bangla(self):
        _word, meaning = self._get_current_entry()
        if not meaning:
            return
        self.stop_event.clear()
        threading.Thread(
            target=self._bangla_speech_worker, args=(meaning,), daemon=True
        ).start()

    def _bangla_speech_worker(self, meaning):
        path = None
        try:
            from gtts import gTTS
            import pygame

            self._set_status("Preparing Bengali voice. Internet connection required...")
            with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as temp:
                path = temp.name

            gTTS(text=meaning, lang="bn", slow=False).save(path)
            if self.stop_event.is_set():
                return

            with self.speech_lock:
                if self.stop_event.is_set():
                    return
                if not self.pygame_mixer_ready:
                    pygame.mixer.init()
                    self.pygame_mixer_ready = True
                pygame.mixer.music.load(path)
                self.bangla_audio_path = path
                pygame.mixer.music.play()

                # Wait without freezing the Tkinter interface.
                while pygame.mixer.music.get_busy() and not self.stop_event.is_set():
                    self.stop_event.wait(0.1)

                try:
                    pygame.mixer.music.stop()
                    pygame.mixer.music.unload()
                except Exception:
                    pass

            self._set_status("Finished speaking Bengali.")
        except ImportError:
            self._show_error(
                "Missing library",
                "Install Bengali speech support with:\npython -m pip install gTTS pygame",
            )
        except Exception as exc:
            if not self.stop_event.is_set():
                self._show_error(
                    "Bengali voice unavailable",
                    "Could not generate or play Bengali speech. Check your internet "
                    "connection and confirm that audio playback is available.\n\n"
                    f"Details: {exc}",
                )
        finally:
            if path and os.path.exists(path):
                try:
                    os.remove(path)
                except OSError:
                    pass
            if self.bangla_audio_path == path:
                self.bangla_audio_path = None

    def stop_voice(self):
        self.stop_event.set()
        try:
            # Stop the active engine without waiting for the speech lock.
            if self.tts_engine is not None:
                self.tts_engine.stop()
        except Exception:
            pass
        try:
            import pygame
            if self.pygame_mixer_ready:
                pygame.mixer.music.stop()
        except Exception:
            pass
        self.status_var.set("Stop requested.")

    def _set_status(self, message):
        try:
            self.root.after(0, lambda: self.status_var.set(message))
        except tk.TclError:
            pass

    def _show_error(self, title, message):
        try:
            self.root.after(0, lambda: messagebox.showerror(title, message, parent=self.root))
        except tk.TclError:
            pass

    def close_app(self):
        self.stop_voice()
        try:
            import pygame
            if self.pygame_mixer_ready:
                pygame.mixer.quit()
        except Exception:
            pass
        self.root.destroy()


def main():
    root = tk.Tk()
    MunimsDictionary(root)
    root.mainloop()


if __name__ == "__main__":
    main()
