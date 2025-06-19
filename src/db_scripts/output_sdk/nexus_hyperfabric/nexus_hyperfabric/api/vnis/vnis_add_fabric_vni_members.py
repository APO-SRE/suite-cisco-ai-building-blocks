from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.common_rest_error import CommonRestError
from ...models.config_fabric_vni_members_response import ConfigFabricVniMembersResponse
from ...models.models_vlan_member import ModelsVlanMember
from ...types import Response


def _get_kwargs(
    fabric_id: str,
    vni_id: str,
    *,
    body: ModelsVlanMember,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/fabrics/{fabric_id}/vnis/{vni_id}/members",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[CommonRestError, ConfigFabricVniMembersResponse]]:
    if response.status_code == 200:
        response_200 = ConfigFabricVniMembersResponse.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = CommonRestError.from_dict(response.json())

        return response_400
    if response.status_code == 401:
        response_401 = CommonRestError.from_dict(response.json())

        return response_401
    if response.status_code == 403:
        response_403 = CommonRestError.from_dict(response.json())

        return response_403
    if response.status_code == 429:
        response_429 = CommonRestError.from_dict(response.json())

        return response_429
    if response.status_code == 500:
        response_500 = CommonRestError.from_dict(response.json())

        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[CommonRestError, ConfigFabricVniMembersResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    fabric_id: str,
    vni_id: str,
    *,
    client: AuthenticatedClient,
    body: ModelsVlanMember,
) -> Response[Union[CommonRestError, ConfigFabricVniMembersResponse]]:
    """Add one or more VNI members.

     Add one or more members to a specific VNI in a fabric.

    Args:
        fabric_id (str):
        vni_id (str):
        body (ModelsVlanMember): A VNI VLAN Member represents the attachement of a specific VNI to
            a port or port channel untagged or using a dot1q VLAN ID (also known as a trunk). The role
            of the port or port channel has to be configured as `HOST_PORT`.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[CommonRestError, ConfigFabricVniMembersResponse]]
    """

    kwargs = _get_kwargs(
        fabric_id=fabric_id,
        vni_id=vni_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    fabric_id: str,
    vni_id: str,
    *,
    client: AuthenticatedClient,
    body: ModelsVlanMember,
) -> Optional[Union[CommonRestError, ConfigFabricVniMembersResponse]]:
    """Add one or more VNI members.

     Add one or more members to a specific VNI in a fabric.

    Args:
        fabric_id (str):
        vni_id (str):
        body (ModelsVlanMember): A VNI VLAN Member represents the attachement of a specific VNI to
            a port or port channel untagged or using a dot1q VLAN ID (also known as a trunk). The role
            of the port or port channel has to be configured as `HOST_PORT`.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[CommonRestError, ConfigFabricVniMembersResponse]
    """

    return sync_detailed(
        fabric_id=fabric_id,
        vni_id=vni_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    fabric_id: str,
    vni_id: str,
    *,
    client: AuthenticatedClient,
    body: ModelsVlanMember,
) -> Response[Union[CommonRestError, ConfigFabricVniMembersResponse]]:
    """Add one or more VNI members.

     Add one or more members to a specific VNI in a fabric.

    Args:
        fabric_id (str):
        vni_id (str):
        body (ModelsVlanMember): A VNI VLAN Member represents the attachement of a specific VNI to
            a port or port channel untagged or using a dot1q VLAN ID (also known as a trunk). The role
            of the port or port channel has to be configured as `HOST_PORT`.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[CommonRestError, ConfigFabricVniMembersResponse]]
    """

    kwargs = _get_kwargs(
        fabric_id=fabric_id,
        vni_id=vni_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    fabric_id: str,
    vni_id: str,
    *,
    client: AuthenticatedClient,
    body: ModelsVlanMember,
) -> Optional[Union[CommonRestError, ConfigFabricVniMembersResponse]]:
    """Add one or more VNI members.

     Add one or more members to a specific VNI in a fabric.

    Args:
        fabric_id (str):
        vni_id (str):
        body (ModelsVlanMember): A VNI VLAN Member represents the attachement of a specific VNI to
            a port or port channel untagged or using a dot1q VLAN ID (also known as a trunk). The role
            of the port or port channel has to be configured as `HOST_PORT`.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[CommonRestError, ConfigFabricVniMembersResponse]
    """

    return (
        await asyncio_detailed(
            fabric_id=fabric_id,
            vni_id=vni_id,
            client=client,
            body=body,
        )
    ).parsed
