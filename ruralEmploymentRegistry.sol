pragma solidity ^0.6.6;


contract RuralEmployRegistry{
    
    bool public status;//contract active or not
    address public owner;//owner here will be the deployer of the SC
    userData[] public userDataList;
    
    mapping (address=>bool) public userDataExists;
    mapping (address=>uint) public userDataIndex;
    mapping (address=>string[]) public skills;
    mapping (address=>uint) public numberOfSkills;
    uint public numberOfRegistrations;
    
    
    struct userData{
        address user_address;
        string first_name;
        string last_name;
        string contact_number;
        string mail_id;
        string DOB;
        string resident_address;
        uint registeration_date;
    }
    
    
    modifier onlyOwner {
        require(msg.sender == owner);
        _;
    }
    
    modifier registeredUsers {
        require(userDataExists[msg.sender]);
        _;
    }
    
    modifier nonRegisteredUsers {
        require(!userDataExists[msg.sender]);
        _;
    }
    
    constructor () public {

        owner=msg.sender;
        status=true;
        owner=msg.sender;
    }
    
    function addAccount(string memory firstName, string memory lastName, string memory contactNumber, string memory mailID, string memory dateOfBirth, string memory residentAddress) nonRegisteredUsers public {
        require(status);//So that only a new user can register, existing users can just update their data...
        
        userDataIndex[msg.sender]=userDataList.length;
        userDataList.push(userData({user_address: msg.sender, first_name: firstName, last_name: lastName, contact_number: contactNumber, mail_id: mailID, DOB: dateOfBirth, resident_address: residentAddress , registeration_date: now }));
        userDataExists[msg.sender]=true;
        numberOfSkills[msg.sender]=0;
        numberOfRegistrations++;
        
    }
        
    function addSkill(string memory enterSkill) registeredUsers public {
        require(status);
        
        skills[msg.sender].push(enterSkill);
        numberOfSkills[msg.sender]++;
    }
    
    function changeStatus() onlyOwner public {
        require(status);
        status=false;//deactivating the smart contract prohibits any function to be executed
    }
    
    
}
