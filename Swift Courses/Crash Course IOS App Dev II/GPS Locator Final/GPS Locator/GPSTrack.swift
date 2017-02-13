//
//  ViewController.swift
//  GPSLocatorApp
//
//  Created by Tingbo Chen on 7/29/16.
//  Copyright © 2016 Tingbo Chen. All rights reserved.
//

import UIKit
import MapKit
import CoreLocation
import Contacts

/*
 To Set Up User location:
 -Build Phases > Link Binary With Libraries > + > CoreLocation.framework
 -In "Info.plist" add:
 -NSLocationWhenInUseUsageDescription  Type: String, Value: Would you like to share your location?
 -NSLocationAlwaysUsageDescription  Type: String, Value: Are you allowing app to access your location?
 */

class GPSTrack: UIViewController, MKMapViewDelegate, CLLocationManagerDelegate, UISearchBarDelegate {
    
    let locationManager = CLLocationManager()
    
    var currentLoc = Dictionary<String, AnyObject>()
    
    @IBOutlet var mapView: MKMapView!
    
    @IBAction func navButtonAction(sender: AnyObject) {
        
        launchNav(currentLoc["lat"] as! CLLocationDegrees, long: currentLoc["long"] as! CLLocationDegrees, addr: currentLoc["addr"] as! String)
        
    }
    
    @IBAction func centerLocButtonAction(sender: AnyObject) {
        
        self.locationManager.requestWhenInUseAuthorization()
        self.locationManager.startUpdatingLocation()
        
    }
    
    @IBAction func coordAlertButtonAction(sender: AnyObject) {
        
        let coord = String(currentLoc["lat"]!) + ", " + String(currentLoc["long"]!)
        
        coordAlert("Coordinates", message: coord)
    
    }
    
    //Coordinates Alert
    func coordAlert(title: String, message: String){
        
        let alert = UIAlertController(title: title, message: message, preferredStyle: UIAlertControllerStyle.Alert)

        alert.addAction(UIAlertAction(title: "OK", style: .Default, handler: { (action) -> Void in
            //self.dismissViewControllerAnimated(true, completion: nil)
            
        }))
        
        self.presentViewController(alert, animated: true, completion: nil)
        
    }
    
    //Time Stamp Extraction
    func timeStampExtraction() -> Dictionary<String, String> {
        
        var timeStamp = Dictionary<String, String>()
        
        let date = NSDate()
        let calendar = NSCalendar.currentCalendar()
        let dateComponents = calendar.components([.Day , .Month , .Year, .Hour, .Minute, .Second], fromDate: date)
        
        let rawList = [dateComponents.day, dateComponents.month, dateComponents.year, dateComponents.hour, dateComponents.minute, dateComponents.second]
        
        var correctedList: [AnyObject] = []
        
        for time in rawList {
            
            var timeCorrection = "00"
            
            if time < 10 {
                timeCorrection = "0"+String(time)
            } else {
                timeCorrection = String(time)
            }
            
            correctedList.append(timeCorrection)
            
        }
        
        timeStamp = ["day" : correctedList[0] as! String, "month" : correctedList[1] as! String, "year" : correctedList[2] as! String, "hour" : correctedList[3] as! String, "minute" : correctedList[4] as! String, "second" : correctedList[5] as! String]
        
        
        return timeStamp
        
    }
    
    //Reverse Geocoder
    func reverseGeocoder(lat: CLLocationDegrees, long: CLLocationDegrees) {
        
        let location_lookup = CLLocation(latitude: lat, longitude: long)
        
        CLGeocoder().reverseGeocodeLocation(location_lookup) { (placemarks, error) -> Void in
            var title = ""
            
            if(error == nil) {
                if let p = placemarks?[0] {
                    var subThoroughfare: String = ""
                    var thoroughfare: String = ""
                    
                    if p.subThoroughfare != nil {
                        subThoroughfare = p.subThoroughfare!
                    }
                    if p.thoroughfare != nil {
                        thoroughfare = p.thoroughfare!
                    }
                    
                    title = "\(subThoroughfare) \(thoroughfare)"
                }
            }
            if title == "" || title == " " {
                title = "Unknown Address"
                
            }
            
            self.navigationController?.navigationBar.topItem?.title = title
            
            //print(String(lat) + "," + String(long))
            
            self.currentLoc["lat"] = lat
            self.currentLoc["long"] = long
            self.currentLoc["addr"] = title
            
            //Printing GPX Code to the logs:
            let timeStamp = self.timeStampExtraction()
            
            let timeStamp_date = timeStamp["year"]! + "-" + timeStamp["month"]! + "-" + timeStamp["day"]!
            
            let timeStamp_time = "T" + timeStamp["hour"]! + ":" + timeStamp["minute"]! + ":" + timeStamp["second"]!
            
            let wpt_top = "<wpt lat=\"" + String(lat) + "\" lon=\"" + String(long) + "\">"
            
            let wpt_mid = "<time>" + timeStamp_date + timeStamp_time + "Z</time>"
            
            let wpt_close = "</wpt>"
            
            let combinedGPX = wpt_top + "\n" + wpt_mid + "\n" + wpt_close
            
            print(combinedGPX)
        }
        
    }
    
    //Launch Navigation
    func launchNav(lat: Double, long: Double, addr: String) {
        
        let SpotLocation = CLLocationCoordinate2DMake(lat, long)
        
        let currentPlacemark = MKPlacemark(coordinate: SpotLocation, addressDictionary: [String(CNPostalAddressStateKey): addr])
        
        let mapItem = MKMapItem(placemark: currentPlacemark)
        
        let launchOptions = [MKLaunchOptionsDirectionsModeKey: MKLaunchOptionsDirectionsModeDriving]
        
        mapItem.openInMapsWithLaunchOptions(launchOptions)
        
    }
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        //Create Map
        self.locationManager.delegate = self
        self.locationManager.desiredAccuracy = kCLLocationAccuracyBest
        self.mapView.delegate = self
        self.mapView.mapType = MKMapType.Standard
        
        self.locationManager.requestWhenInUseAuthorization()
        self.locationManager.startUpdatingLocation()
        self.mapView.showsUserLocation = true
        
    }

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        
    }
    
    //Function for Updating User location to center on User:
    func locationManager(manager: CLLocationManager, didUpdateLocations locations: [CLLocation]) {
        
        //Location Zoom
        let location = locations.last
        let user_location = CLLocationCoordinate2D(latitude: location!.coordinate.latitude, longitude: location!.coordinate.longitude)
        let region = MKCoordinateRegion(center: user_location, span: MKCoordinateSpan(latitudeDelta: 0.01, longitudeDelta: 0.01))
        self.mapView.setRegion(region, animated: true)
        
        //Stops updating
        self.locationManager.stopUpdatingLocation()
        
        //Remove existing Annotations
        let annotationsToRemove = mapView.annotations.filter { $0 !== self.mapView.userLocation }
        self.mapView.removeAnnotations(annotationsToRemove)
        
        //Adds an Annotation
        let annotation = MKPointAnnotation()
        annotation.coordinate = user_location
        //annotation.title = "New Place"
        //annotation.subtitle = "One day I'll own here..."
        self.mapView.addAnnotation(annotation)
        
        //Reverse Geocoder to get the address:
        reverseGeocoder(annotation.coordinate.latitude, long: annotation.coordinate.longitude)
            
    }
    
    //Function allow User to drag annotation:
    func mapView(mapView: MKMapView, viewForAnnotation annotation: MKAnnotation) -> MKAnnotationView? {
        if annotation is MKUserLocation {
            return nil
        }
        
        let reuseId = "pin"
        var pinView = mapView.dequeueReusableAnnotationViewWithIdentifier(reuseId) as? MKPinAnnotationView
        if pinView == nil {
            pinView = MKPinAnnotationView(annotation: annotation, reuseIdentifier: reuseId)
            pinView?.draggable = true
        }
        else {
            pinView?.annotation = annotation
        }
        
        return pinView
    }
    
    //Function gets dropped annotation's location:
    func mapView(mapView: MKMapView, annotationView view: MKAnnotationView, didChangeDragState newState: MKAnnotationViewDragState, fromOldState oldState: MKAnnotationViewDragState) {
        
        if newState == MKAnnotationViewDragState.Ending {
            
            let droppedAt = view.annotation?.coordinate
            
            //Reverse Geocoder to get the address:
            reverseGeocoder(droppedAt!.latitude, long: droppedAt!.longitude)
            }
    }
}


