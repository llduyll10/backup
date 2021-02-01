import React, { Component } from 'react'
import { View, Text, Image, StyleSheet, Dimensions, ImageBackground } from 'react-native'
export default class HeaderUI extends Component {
    render() {
        return (
            <View style={styles.container}>
                <View style={styles.coverLeft}>
                    <Image style={styles.avatar} source={{ uri: 'https://s3.amazonaws.com/uifaces/faces/twitter/ladylexy/128.jpg' }} />
                    <View style={styles.coverText}>
                        <Text style={styles.name}>Nguyen Duy</Text>
                        <Text>Thành viên Kim Cương | 1387</Text>
                    </View>
                </View>
                <View style={styles.coverRight}>
                    <Text>Right</Text>
                </View>
            </View>
        )
    }
}
const styles = StyleSheet.create({
    container: {
        flex: 1,
        justifyContent: "space-around",
        flexDirection: 'row'
    },
    coverLeft: {
        flex: 1,
        justifyContent: 'flex-start',
        flexDirection: 'row',
        marginLeft:10
    },
    coverRight: {
        flex: 1,
        justifyContent: 'flex-end',
        flexDirection: 'row'
    },
    avatar: {
        width: 50,
        height: 50,
        borderRadius: 50 / 2
    },
    coverText:{
        marginLeft:3,
        paddingTop:5,
    },
    name:{
        fontSize:15,
        fontWeight:'bold',
        marginBottom:2
    }
})