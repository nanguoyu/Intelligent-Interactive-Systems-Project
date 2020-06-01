package furhatos.app.iisproject.flow

import furhatos.flow.kotlin.State
import furhatos.flow.kotlin.furhat
import furhatos.flow.kotlin.onResponse
import furhatos.flow.kotlin.state
import furhatos.gestures.Gestures
import furhatos.nlu.common.No
import furhatos.nlu.common.Yes
import khttp.responses.Response
import java.io.File
import java.util.*
import javax.swing.ImageIcon
import javax.swing.JFrame
import javax.swing.JLabel

val Start : State = state(Interaction) {
    onEntry {
        furhat.ask("Hi there. Shall we start to play 'Rock Paper Scissors Lizard Spock'?")
    }
    onResponse<Yes>{
        furhat.say("Let's start!")
        furhat.gesture(Gestures.Smile(duration = 2.0, strength = 1.0))
        delay(500)
        goto(RPSLS)
    }
    onResponse<No>{
        furhat.say("See you next time!")
        furhat.gesture(Gestures.Smile(duration = 2.0, strength = 1.0))
    }
}

var round = 0 // count the game round
var RPSLS : State = state(Interaction) {
    onEntry {
        round += 1
        furhat.say("Round $round")
        goto(play)
    }
//    if continue the game
    onReentry {
        round += 1
        furhat.say("Round $round")
        goto(play)
    }
}

var totalFlag = 0 // positive: user wins, negative: Furhat wins
val play : State = state(Interaction) {
    val gesture = "paper,rock,scissors,lizard,spock"
    val gestures: List<String> = gesture.split(",")
    onEntry {
        val rand1 = Random()
//        randomly select one frame as user's input
        val randNum1: Int = rand1.nextInt(14399 - 0 + 1) + 0
        val path = "/Users/vera/Desktop/imgs/img_$randNum1.png"
//        show the image
        val frame = JFrame()
        val icon = ImageIcon(path)
        val label = JLabel(icon)
        frame.add(label)
        frame.setDefaultCloseOperation(JFrame.DO_NOTHING_ON_CLOSE)
        frame.pack()
        frame.setVisible(true)
//        post the image to the server
        val file = File(path)
        val encode = Base64.getEncoder().encodeToString(file.readBytes())
        val response: Response = khttp.post(url = "http://127.0.0.1:5000/end2end", data = mapOf("image" to encode))
//        val response: Response = khttp.post(url = "http://127.0.0.1:5000/gesture", data = mapOf("image" to encode))
        val message = response.content.toString(Charsets.UTF_8)
        val subMessage: List<String> = message.split(":", ",")
//    game gesture
        var flagU = gestures[0]
//    game rules: p>r, s>p, sp>s, l>sp, r>l, l>p, p>sp, sp>r, r>s, s>l
        var flag = 0 // positive: user wins, negative: Furhat wins
        if (subMessage[1].equals("200")) {
//            robot give a random gesture
            when (subMessage[3]) {
                "\"open_dorsal\"" -> {
//                  paper
                    flagU = gestures[0]
                }
                "\"open_palm\"" -> {
//                  lizard
                    flagU = gestures[3]
                }
                "\"fist_palm\"" -> {
//                  spock
                    flagU = gestures[4]
                }
                "\"fist_dorsal\"" -> {
//                  rock
                    flagU = gestures[1]
                }
                "\"three_fingers_palm\"" -> {
//                  random
                    val rand2 = Random()
                    val randNum2: Int = rand2.nextInt(4 - 0 + 1) + 0
                    flagU = gestures[randNum2]
                }
                "\"three_fingers_dorsal\"" -> {
//                  scissors
                    flagU = gestures[2]
                }
            }
            furhat.say("User gives $flagU.")
            val rand3 = Random()
            val randNum3: Int = rand3.nextInt(4 - 0 + 1) + 0
            val flagF = gestures[randNum3]
            furhat.say("Furhat gives $flagF.")
            if(flagU.equals(gestures[0])) {
                if(flagF.equals(gestures[1])) {
                    flag += 1
                }
                else if(flagF.equals(gestures[2])) {
                    flag -= 1
                }
                else if(flagF.equals(gestures[3])) {
                    flag -= 1
                }
                else if(flagF.equals(gestures[4])) {
                    flag += 1
                }
            }
            else if(flagU.equals(gestures[1])) {
                when {
                    flagF.equals(gestures[0]) -> {
                        flag -= 1
                    }
                    flagF.equals(gestures[3]) -> {
                        flag += 1
                    }
                    flagF.equals(gestures[4]) -> {
                        flag -= 1
                    }
                    flagF.equals(gestures[2]) -> {
                        flag += 1
                    }
                }
            }
            else if(flagU.equals(gestures[2])) {
                when {
                    flagF.equals(gestures[0]) -> {
                        flag += 1
                    }
                    flagF.equals(gestures[4]) -> {
                        flag -= 1
                    }
                    flagF.equals(gestures[1]) -> {
                        flag -= 1
                    }
                    flagF.equals(gestures[3]) -> {
                        flag += 1
                    }
                }
            }
            else if(flagU.equals(gestures[3])) {
                when {
                    flagF.equals(gestures[4]) -> {
                        flag += 1
                    }
                    flagF.equals(gestures[1]) -> {
                        flag -= 1
                    }
                    flagF.equals(gestures[0]) -> {
                        flag += 1
                    }
                    flagF.equals(gestures[2]) -> {
                        flag -= 1
                    }
                }
            }
            else {
                if(flagF.equals(gestures[2])) {
                    flag += 1
                }
                else if(flagF.equals(gestures[3])) {
                    flag -= 1
                }
                else if(flagF.equals(gestures[0])) {
                    flag -= 1
                }
                else if(flagF.equals(gestures[1])) {
                    flag += 1
                }
            }
        }
        if(flag>0) {
            furhat.say("User wins.")
        }
        else if(flag<0) {
            furhat.say("Furhat wins.")
        }
        else {
            furhat.say("The game ties.")
        }
        totalFlag += flag
        frame.dispose()
        furhat.ask("Do you want to continue the game?")
    }
    onResponse<Yes>{
        goto(RPSLS)
    }
    onResponse<No>{
        if(totalFlag>0) {
            furhat.say("After all the games, user wins.")
        }
        else if(totalFlag<0) {
            furhat.say("After all the games, Furhat wins.")
        }
        else{
            furhat.say("After all, the game ties.")
        }
        furhat.say("See you next time!")
        furhat.gesture(Gestures.Smile(duration = 2.0, strength = 1.0))
        System.exit(0)
    }
}
