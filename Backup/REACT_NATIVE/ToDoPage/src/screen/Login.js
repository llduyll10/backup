import React, { Component } from 'react'
import { Text, View, SafeAreaView, StyleSheet, Button, TextInput, KeyboardAvoidingView } from 'react-native'

export default class LoginScreen extends Component {
    static navigationOptions = {
        header: null
    }
    state = {
        email: '',
        password: ''
    }
    render() {
        const { email, password } = this.state
        const {navigate} = this.props.navigation
        return (
            <SafeAreaView style={styles.container}>
                <KeyboardAvoidingView
                    behavior="padding"
                    keyboardVerticalOffset={0}
                    style={{ flex: 1 }}
                    enabled={Platform.OS == 'ios' ? true : false}
                >
                    <View style={styles.coverContent}>
                        <TextInput style={styles.inputLogin} value={email} placeholder="Email"/>
                        <TextInput style={styles.inputLogin} value={password} placeholder="Password"/>
                        <Button title="Đăng nhập"/>
                        <Button title="Đăng ký" onPress={()=>navigate('Si')}/>
                    </View>
                </KeyboardAvoidingView>
            </SafeAreaView>

        )
    }
}
const styles = StyleSheet.create({
    container: {
        flex: 1,
    },
    coverContent: {
        flex: 1,
        alignItems: "center",
        justifyContent: "center"
    },
    inputLogin:{
       backgroundColor:'white',
       width:'80%',
       borderRadius:10,
       margin:10,
       padding:5,
       height:40,
       borderColor:'grey',
       borderWidth:1
    }
})