# Covenant Services Query with EnumServiceStatusW

## Metadata


|                       |    |
|:----------------------|:---|
| id                    | SDWIN-200806012009 |
| author                | Roberto Rodriguez @Cyb3rWard0g |
| creation date         | 2020/08/06 |
| platform              | Windows |
| Simulaton Environment | Mordor shire |
| Simulation Scripts    | [] |
| Dataset           | https://raw.githubusercontent.com/OTRF/mordor/master/datasets/small/windows/lateral_movement/covenant_sharpsc_dcerpc_smb_svcctl_EnumServiceStatusW.zip |
| References        | None |

## Dataset Description
This dataset represents a threat actor with network access to the service control manager (SCM) service over SMB of another enpoint in the network executing the EnumServiceStatusW method to get information about services.

## Adversary View
```
(wardog) > SharpSC /command:"action=query computername=WORKSTATION6 service=ikeext"

[+] Service information for IKEEXT on WORKSTATION6:

  DisplayName: IKE and AuthIP IPsec Keying Modules

  ServiceName: IKEEXT

  Status     : Stopped

  CanStop    : False
```

## Explore Mordor Dataset

### Initialize Analytics Engine

from openhunt.mordorutils import *
spark = get_spark()

### Download & Process Mordor File

mordor_file = "https://raw.githubusercontent.com/OTRF/mordor/master/datasets/small/windows/lateral_movement/covenant_sharpsc_dcerpc_smb_svcctl_EnumServiceStatusW.zip"
registerMordorSQLTable(spark, mordor_file, "mordorTable")

### Get to know your data

df = spark.sql(
    '''
SELECT *
FROM mordorTable
    '''
)
df.printSchema()
        