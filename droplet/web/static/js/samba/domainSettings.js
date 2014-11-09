function domainSettingsController($scope, $http) {
    $scope.formData = {};

    $http.get("/samba/settings").success(function (response) {
        $scope.modeOptions = [ { value: 'dc', name: 'Domain controller'}, { value: 'ad', name: 'Domain member' } ];
        var data = response[0];
        $scope.formData = {
            domain: data.domain,
            workgroup: data.workgroup,
            mode: data.mode,
            realm: data.realm,
            netbios: data.netbios,
            description: data.description
        };

    });

    $scope.processForm = function () {
        $http.post("/samba/settings/", $scope.formData, {}).success(function (dataFromServer, status, headers, config) {
          console.log("Form submitted successfully");
        }).error(function(data, status, headers, config) {
          alert("Submitting form failed!");
        });
    };
}

function DomainMenu($scope, $http) {
    $scope.menus = [
        {
            label: 'Domain',
            open: false,
            items: [
                { label: 'Settings' },
            ]
        }
    ];
}
