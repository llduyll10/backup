import React, { Component } from 'react'
import { View, Text, StyleSheet, SafeAreaView } from 'react-native'
export default class NotificationScreen extends Component {
    static navigationOptions = {
        header: null
    }
    render() {
        return (
            <SafeAreaView style={styles.container}>
                <View>
                    <Text>Notification</Text>
                </View>
            </SafeAreaView>

        )
    }
}

const styles = StyleSheet.create({
    container:{
        flex:1,
        justifyContent:'center',
        alignItems:'center'
    }
})