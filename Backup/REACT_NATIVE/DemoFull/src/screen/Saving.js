import React, { Component } from 'react'
import { View, Text, StyleSheet, SafeAreaView, ScrollView, KeyboardAvoidingView, Platform, Button, Animated } from 'react-native';
import { Tab, Tabs } from 'native-base';
import NoAuth from '../component/NoAuth'
export default class SavingScreen extends Component {
    static navigationOptions = {
        header: null
    }
    render() {
        return (
            <SafeAreaView style={styles.container}>
                <View style={styles.coverHeader}>
                    <Text style={styles.textHeader}>SAVING</Text>
                </View>
                <Tabs>
                    <Tab heading="Tất cả">
                        <NoAuth />
                    </Tab>
                    <Tab heading="Địa điểm">
                        <NoAuth />
                    </Tab>
                    <Tab heading="Hình ảnh">
                        <NoAuth />
                    </Tab>
                    <Tab heading="Bài viết">
                        <NoAuth />
                    </Tab>
                </Tabs>
            </SafeAreaView>
        )
    }
}

const styles = StyleSheet.create({
    container: {
        flex: 1
    },
    coverHeader: {
        backgroundColor: 'red',
        width: '100%',
        height: 50,
        flexDirection: 'row',
        justifyContent: 'center',
        alignItems: "center"
    },
    textHeader: {
        color: 'white',
        fontWeight: 'bold',
        fontSize: 15
    }
})