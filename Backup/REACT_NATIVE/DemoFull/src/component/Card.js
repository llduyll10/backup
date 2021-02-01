import React from 'react';
import { View, Text, Button, StyleSheet, SafeAreaView, FlatList, Image } from 'react-native';
export default class OptionCard extends React.Component {
    static navigationOptions = {
        title: 'Home'
    }
    state = {
        dataImg: [
            {
                key: 'https://topship.vn/uploads/1558169502_1557215946_123rf_80109192_mega_[converted]_2.png',
                name: 'Giao hàng'
            },
            {
                key: 'http://genknews.genkcdn.vn/thumb_w/640/2013/Untitled-66dd9.png',
                name: 'Tìm kiếm'
            },
            {
                key: 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQpd5feUFm1-wxafSuyd4IvEh7s3exxo18TNrQhkqSZz7OvIytrjg&s',
                name: 'Đặt chỗ'
            }
        ]
    }
    render() {
        const { navigation } = this.props
        return (
            <View style={styles.container}>
                {
                    this.state.dataImg.map((item,i)=>(
                        <Card uri={item.key} key={item.key} name={item.name}/>
                    ))
                }
            </View>

        );
    }
}
const Card = props => {
    return (<View style={styles.card}>
        <Image style={styles.image} source={{ uri: props.uri }} />
        <Text style={styles.text}>{props.name}</Text>
    </View>)
}
const styles = StyleSheet.create({
    container: {
        flexDirection: 'row',
        justifyContent: 'space-around'
    },
    card: {
        flexDirection: 'column',
        alignItems:'center',
        justifyContent:'center'
    },
    image: {
        width: 100,
        height: 100
    },
    text:{
       paddingTop:3,
       fontSize:15
    }
});