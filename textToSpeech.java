import com.sun.speech.freetts.Voice;
import com.sun.speech.freetts.VoiceManager;

public class TextToSpeechConverter {

    public static void convertTextToSpeech(String text, String voiceName) {
        VoiceManager voiceManager = VoiceManager.getInstance();
        Voice voice = voiceManager.getVoice(voiceName);

        if (voice != null) {
            voice.allocate();
            voice.speak(text);
            voice.deallocate(); // Deallocate the voice resources after use
        } else {
            System.err.println("Cannot find the specified voice.");
        }
    }

    public static void main(String[] args) {
        String text = "Hello, this is a test for text to speech conversion.";
        String voiceName = "kevin16"; // or other available voice name

        convertTextToSpeech(text, voiceName);
    }
}
