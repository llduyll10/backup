import React from 'react';
import Carousel from 'react-native-banner-carousel';
import { StyleSheet, Image, View, Dimensions } from 'react-native';

const BannerWidth = Dimensions.get('window').width;
const BannerHeight = 260;

const images = [
    {
        location:require('../img/banner1.jpg')
    },
    {
        location:require('../img/banner2.jpg')
    },
    {
        location:require('../img/banner3.jpg')
    },
];

export default class App extends React.Component {
    renderPage(image, index) {
        return (
            <View key={index} >
                <Image style={{ width: BannerWidth, height: BannerHeight, }} source={image.location} />
            </View>
        );
    }

    render() {
        return (
            <View style={styles.container}>
                <Carousel
                    autoplay
                    autoplayTimeout={3000}
                    loop
                    index={0}
                    pageSize={BannerWidth}
                >
                    {images.map((image, index) => this.renderPage(image, index))}
                </Carousel>
            </View>
        );
    }
}

const styles = StyleSheet.create({
    container: {
        flex: 1,
        justifyContent: 'center',
    },
});

// state = {
//     dataImg: [
//         'https://vnn-imgs-f.vgcloud.vn/2019/05/03/11/co-gai-khien-hot-girl-tram-anh-bi-lu-mo-vi-qua-xinh-dep-3.jpg',
//         'https://media.ngoisao.vn/resize_580/news/2018/11/26/hotgirl-1-ngoisao.vn-w600-h493.jpg',
//         'https://vnn-imgs-a1.vgcloud.vn/znews-photo.zadn.vn/w660/Uploaded/mdf_uswreo/2019_07_15/namkhingkanyapak_60426835_412316679355836_7226004449756221104_n.jpg'
//     ]
// }

