#!/usr/bin/python
import json,zipfile

class project:
    def __init__(self,projectFilePath):
        #Open ZIP
        self.zip_ref=zipfile.ZipFile(projectFilePath)

        #Load json files to memory
        self.jsonFloorPlans              =json.loads(self.zip_ref.read("floorPlans.json"))
        self.jsonAccessPoints            =json.loads(self.zip_ref.read("accessPoints.json"))
        if "measuredRadios.json" in self.zip_ref.namelist():
            self.jsonMeasuredRadios=json.loads(self.zip_ref.read("measuredRadios.json"))
        else:
            self.jsonMeasuredRadios=""
        if "accessPointMeasurements.json" in self.zip_ref.namelist():
            self.jsonAccessPointMeasurements=json.loads(self.zip_ref.read("accessPointMeasurements.json"))
        else:
            self.jsonAccessPointMeasurements=""

        #Load additional files to memory
        #Floorplans:
        self.fpBitmap={}
        for fp in self.jsonFloorPlans["floorPlans"]:
            self.fpBitmap[fp["id"]] = fp["imageId"]

'''
#SCHEMA DOCUMENTATION
##accessPoints.json 8/15/2018:
{
 "$schema": "http://json-schema.org/schema#",
 "required": [
  "accessPoints"
 ],
 "type": "object",
 "properties": {
  "accessPoints": {
   "items": {
    "required": [
     "id",
     "location",
     "mine",
     "name",
     "status",
     "userDefinedPosition"
    ],
    "type": "object",
    "properties": {
     "status": {
      "type": "string"
     },
     "name": {
      "type": "string"
     },
     "mine": {
      "type": "boolean"
     },
     "location": {
      "required": [
       "coord",
       "floorPlanId"
      ],
      "type": "object",
      "properties": {
       "floorPlanId": {
        "type": "string"
       },
       "coord": {
        "required": [
         "x",
         "y"
        ],
        "type": "object",
        "properties": {
         "y": {
          "type": "number"
         },
         "x": {
          "type": "number"
         }
        }
       }
      }
     },
     "id": {
      "type": "string"
     },
     "userDefinedPosition": {
      "type": "boolean"
     }
    }
   },
   "type": "array"
  }

##floorPlans.json 8/15/2018:
{
 "$schema": "http://json-schema.org/schema#",
 "required": [
  "floorPlans"
 ],
 "type": "object",
 "properties": {
  "floorPlans": {
   "items": {
    "required": [
     "floorPlanType",
     "height",
     "id",
     "imageId",
     "metersPerUnit",
     "name",
     "status",
     "width"
    ],
    "type": "object",
    "properties": {
     "metersPerUnit": {
      "type": "number"
     },
     "status": {
      "type": "string"
     },
     "name": {
      "type": "string"
     },
     "legacyId": {
      "type": "integer"
     },
     "imageId": {
      "type": "string"
     },
     "width": {
      "type": "number"
     },
     "floorPlanType": {
      "type": "string"
     },
     "height": {
      "type": "number"
     },
     "id": {
      "type": "string"
     }
    }
   },
   "type": "array"
  }
 }
}

'''
