import React,{Component} from 'react'
import {View,Text} from 'react-native'
export default class SigninScreen extends Component{
    static navigationOptions = {
        header:null
    }
    render(){
        return(
            <View>
                <Text>Login</Text>
            </View>
        )
    }
}