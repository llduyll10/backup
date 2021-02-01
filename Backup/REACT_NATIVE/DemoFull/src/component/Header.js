import React, { Component } from 'react';
import { AppRegistry, TextInput, StyleSheet, View, Dimensions,Button } from 'react-native';
const DEVICE_WIDTH = Dimensions.get('window').width
export default class SearchBarExample extends Component {
    state = {
        text: +'   Tìm kiếm món ăn,tên địa điểm, địa chỉ'
    }
    render() {
        return (
            <View style={styles.conatainer}>            
                <TextInput
                    style={styles.textSearch}
                    onChangeText={(text) => this.setState({ text })}
                    value={this.state.text}
                />
            </View>
        );
    }
}
const styles = StyleSheet.create({
    conatainer: {
        width: DEVICE_WIDTH,
        height: 50,
        flexDirection:'row',
        justifyContent:"center",
        alignItems:'center',
        backgroundColor:'red',
        padding:0
    },
    textSearch: {
        height: 30,
        borderColor: 'gray',
        borderWidth: 1,
        padding: 0,
        width:'90%',
        borderRadius:5,
        backgroundColor:'white',
        fontSize:13
    },


})